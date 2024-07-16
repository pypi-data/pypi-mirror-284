#!/usr/bin/env python
# Copyright Salient Predictions 2024

"""Skill and validation."""

import numpy as np
import pandas as pd
import xarray as xr


def crpss(forecast: xr.DataArray, reference: xr.DataArray) -> xr.DataArray:
    """Continuous Ranked Probability Skill Score.

    CRPSS measures the relative skill improvement of one CRPS forecast over another.
    Positive values can roughly interpreted as percentages, so a CRPSS of 0.10 means a 10% improvement.
    Zero values mean no improvement, and negative values mean the forecast is worse than the reference.

    Args:
        forecast: The forecast data
        reference: The reference baseline data

    Returns:
        xr.DataArray: The CRPSS result
    """
    skill_score = 1 - (forecast / reference)

    if "long_name" in forecast.attrs:
        skill_score.attrs["long_name"] = forecast.attrs["long_name"] + " Skill"

    if isinstance(skill_score, xr.DataArray):
        skill_score.name = "crpss"

    return skill_score


def _convert_to_lead(ds):  # , forecast_date="forecast_date"):
    """Convert 'time' coordinate to 'lead' starting from 1."""
    lead_times = np.arange(1, ds.sizes["time"] + 1)
    ds = ds.assign_coords(lead=("time", lead_times))
    ds = ds.swap_dims({"time": "lead"})
    ds = ds.drop_vars("time")
    return ds


def _align_coords(observations: xr.DataArray, forecasts: xr.DataArray) -> xr.DataArray:
    """Ensure that the coordinates of two xarrays are comparable.

    Generally to calculate skill scores, the coordinates of `observations` must
    be a strict subset of the coordinates of `forecasts`.  This function will
    attempt to coerce the coordinates of `observations` to match those of `forecasts`.

    The most common use case is to transform daily `observations` to match
    `forecasts` denominated with a more coarse timescale.

    Args:
        observations (xr.DataArray): observed values
        forecasts (xr.DataArray): forecast values

    Returns:
        xr.DataArray: `observations` with the same dimension as the forecasts.
    """
    # Save memory by opening the observations dataset for each individual forecast file
    # if isinstance(observations, str):
    #    with xr.open_dataset(observations) as obs_ds:
    #        return _align_coords(obs_ds, forecasts)

    def assert_daily(observations):
        assert (observations.time.values[1] - observations.time.values[0]).astype(
            "timedelta64[D]"
        ) == 1, "Observations must be daily when time dimensions don't match."

    # if the coordinates of observations are a strict subset of the coordinates of forecasts,
    # return early.  No operations needed.
    if (
        "time" in forecasts.dims
        and "time" in observations.dims
        and not forecasts.time.identical(observations.time)
    ):
        assert_daily(observations)
        time = forecasts.time.values
        # 7d weekly, 30d monthly, 90d quarterly
        days = (time[1] - time[0]).astype("timedelta64[D]")
        bins = np.append(time, time[-1] + days)

        observations = (
            observations.groupby_bins("time", bins, right=True)
            .mean()
            .assign_coords(time=("time_bins", time))
            .swap_dims({"time_bins": "time"})
            .drop_vars("time_bins")
        )
    elif "lead_weekly" in forecasts.coords and "time" in observations.coords:
        assert_daily(observations)

        lead_name = "lead_weekly"
        date_name = "forecast_date_weekly"
        lead_size = 7

        fcst_date = forecasts[date_name].values
        lead_vals = forecasts[lead_name].values
        bins = fcst_date + np.array(lead_size * np.append(0, lead_vals), dtype="timedelta64[D]")
        observations = (
            observations.groupby_bins("time", bins)
            .mean()
            .assign_coords(lead=("time_bins", lead_vals))
            .rename({"lead": lead_name})
            .swap_dims({"time_bins": lead_name})
            .drop_vars("time_bins")
        )

    return observations


def crps(
    observations: xr.DataArray | xr.Dataset | str,
    forecasts: xr.DataArray | xr.Dataset | str | list[str] | pd.DataFrame,
    qnt_dim: str = "quantiles",
) -> xr.DataArray | xr.Dataset:
    """Calculate Continuous Ranked Probability Score.

    CRPS is used to calculate the skill of a probabilistic forecast.
    CRPS is defined as 2 times the integral of the quantile loss over the distribution.
    Zero CRPS indicates a perfect forecast.

    Args:
        observations: `DataArray` of observed values, aka "truth", or a `nc` filename.
            `observations` should usually have the same coordinates as `forecasts`.
            If `observations` has a `daily` timescale to match
            a `weekly`, `monthly`, or `quarterly` timescale for `forecasts.`
        forecasts: `DataArray` of forecasted values.  May also be:
          * a file reference to a `nc` file
          * a vector of file references to `nc` files
          * a DataFrame with a `file_name` column
        qnt_dim: Name of the quantile dimension in the forecast array.

    Returns:
        The CRPS of the forecasted values vs the observations.

    """
    if isinstance(observations, str):
        observations = xr.load_dataarray(observations)

    if isinstance(forecasts, str):
        forecasts = xr.load_dataarray(forecasts)
    elif isinstance(forecasts, pd.DataFrame):
        assert "file_name" in forecasts.columns, "DataFrame must have 'file_name' column."
        return crps(observations, forecasts["file_name"].tolist(), qnt_dim)
    elif isinstance(forecasts, list):
        skill = [crps(observations, fcst, qnt_dim) for fcst in forecasts]
        if "time" in skill[0].coords:
            # Calc the average by relative lead, not by absolute date.
            # should this just be in _align_coords?
            skill = [_convert_to_lead(s) for s in skill]

        # TODO: determine concat_dim dynamically
        # concat_dim = "forecast_date"
        concat_dim = "forecast_date_weekly"
        skill = xr.concat(skill, dim=concat_dim)
        skill = skill.mean(dim=concat_dim, keep_attrs=True)

        return skill
    elif not isinstance(forecasts, xr.DataArray):
        raise ValueError(
            f"forecast {type(forecasts)} must be a DataArray, DataFrame[file_name], or filename."
        )

    observations = _align_coords(observations, forecasts)

    # This is the primary CRPS calculation.  Everything else is just coordinate coercion
    # qnt_val = forecasts[qnt_dim]
    diff = observations - forecasts
    qnt_val = diff[qnt_dim]
    qnt_score = 2 * np.maximum(qnt_val * diff, (qnt_val - 1) * diff)
    skill = qnt_score.integrate(coord=qnt_dim)

    if "long_name" in forecasts.attrs:
        skill.attrs["long_name"] = forecasts.attrs["long_name"] + " CRPS"
    if "units" in forecasts.attrs:
        skill.attrs["units"] = forecasts.attrs["units"]

    if isinstance(skill, xr.DataArray):
        skill.name = "crps"

    return skill
