#!usr/bin/Python3
"""
This script prompts measurement update and reruns the inference which
has already run by './funzler_start.py'.
"""

import numpy as np
import pandas as pd
import yaml
from funzler_start import explanability_check, run


def prompt_and_update_meas(input_df):
    """prompt user updates on measurement and update measurement column in input_df
    """
    # user input (new_meas_array) format: [id value id value id value ...]
    new_meas_array = np.fromstring(
        input("Enter updated boundary measurement:"), dtype=float, sep=' ')
    # TODO currently no exception handling
    n_meas = int(new_meas_array.shape[0]/2)
    meas = input_df[["measurement", "meas_type"]].values
    for i in range(n_meas):
        meas[int(new_meas_array[2*i]), :] = [new_meas_array[2*i+1], "manual"]
    input_df[["measurement", "meas_type"]] = meas


def main():
    # Load input and output dataframes from the last run
    input_df = pd.read_csv('_tmp_input.csv').drop(columns=['Unnamed: 0'])
    # Convert string "dict" into dict
    param_dict = yaml.load(input_df["configs"][2])
    input_df["configs"][2] = param_dict

    # Prompt user updates for measurement and re-run
    prompt_and_update_meas(input_df)
    run(input_df)


if __name__ == "__main__":
    main()