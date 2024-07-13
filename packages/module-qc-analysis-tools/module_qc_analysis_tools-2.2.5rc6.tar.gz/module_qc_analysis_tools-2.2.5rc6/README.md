# module-qc-analysis-tools v2.2.5rc6

A general python tool for running ITkPixV1.1 module QC test analysis. An
overview of the steps in the module QC procedure is documented in the
[Electrical specification and QC procedures for ITkPixV1.1 modules](https://gitlab.cern.ch/atlas-itk/pixel/module/itkpix-electrical-qc/)
document and in
[this spreadsheet](https://docs.google.com/spreadsheets/d/1qGzrCl4iD9362RwKlstZASbhphV_qTXPeBC-VSttfgE/edit#gid=989740987).
The analysis scripts in this repository require input files with measurement
data. The measurement data should be collected using the
[module-qc-measurement-tools](https://gitlab.cern.ch/atlas-itk/pixel/module/module-qc-tools)
package.

## Table of contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Scripts](#scripts)
   1. [IV Measurement](#sensor_iv_measurement)
   2. [ADC calibration](#adc_calibration)
   3. [Analog readback](#analog_readback)
   4. [SLDOVI](#sldo)
   5. [VCal calibration](#vcal_calibration)
   6. [Injection capacitance](#injection_capacitance)
   7. [Low Power Mode](#lp_mode)
   8. [Overvoltage Protection](#overvoltage_protection)
   9. [Undershunt Protection](#undershunt_protection)
   10. [Data transmission](#data_transmission)
   11. [Minimum health](#minimum_health)
   12. [Tuning performance](#tuning_performance)
   13. [Pixel failure](#pixel_failure)
4. [Notes](#notes)
   1. [Submit QC results](#submit-qc-results)
   2. [Example commands](#example-commands-for-a-chip-in-a-quad-module-L2)
   3. [Update chip config](#update-chip-config)
   4. [Load YARR scans](#load-yarr-scans)
5. [For developer](#for-developer)

## Requirements

This tool requires users to have >python3.6 with the following packages
installed:

- `numpy`
- `scipy`
- `tabulate`
- `matplotlib`
- `jsonschema`

## Installation

This package may be accessed by cloning from gitlab or by installing it via pip.

### via clone

Use this method if you want to use the latest version of the package from
gitlab. First clone the project:

```
git clone https://gitlab.cern.ch/atlas-itk/pixel/module/module-qc-analysis-tools.git
```

Upon a successful checkout, `cd` to the new `module-qc-analysis-tools` directory
and run the following to install the necessary software:

```bash
$ python3 -m venv env
$ source env/bin/activate
$ python -m pip install --upgrade pip
$ python -m pip install -e .
```

### via pip

Use this method if you want to use the latest stable (versioned) release of the
package.

```bash
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -U pip
$ python -m pip install -U pip module-qc-analysis-tools==2.2.5rc6
```

Note that users should use the latest python version (check python version via
`python3 -V`). Python3.7 is the minimum requirement for developers. See
[For Developer](#for-developer) section.

## Scripts

### `Sensor IV Measurement`

This analysis script analyses sensor leakage current vs voltage measurement. It
produces an output file with several key parameters: breakdown voltage, leakage
current at operation voltage (depletion voltage + 20/50V for 3D/planar sensor),
whether breakdown was observed and the absolute maximum measured bias voltage.
Note that raw measurement data will be plotted and uploaded onto the production
database, which uses the absolute bias voltage and leakage current regardless of
the polarity. All currents will be converted to uA.

If the depletion voltage if the sensor is unknown, please do not supply anything
to `--vdepl`. In this case either a value from the database or a default value
will be used.

One analysis criterion is the change wrt the bare module stage. For this, an
additional input file is required which provides the reference bare module IV
with up to 3 bare modules (triplets) in the format below. This is generated in
localDB. If none is supplied, the analysis will run but the module will not
pass.

<details> <summary> Bare Module IV format </summary>
```
{
  'target_component' : <MODULE_SN>,
  'target_stage' : <MODULE_STAGE>,
  'reference_IVs' : [
    { 'component' : <SENSOR_TILE_SN>,
      'stage' : <bare module stage>,
      'Vbd' : <VALUE>,
      'Vfd' : <VALUE>,
      'temperature' : <VALUE>,
      'IV_ARRAY' : { "voltage" : [ array ], "current" : [array], "temperature": [array] }
    },
    { 'component' : <SENSOR_TILE_SN>,
      'stage' : <bare module stage>,
      'Vbd' : <VALUE>,
      'Vfd' : <VALUE>,
      'temperature' : <VALUE>,
      'IV_ARRAY' : { "voltage" : [ array ], "current" : [array], "temperature": [array] }
    },
    { 'component' : <SENSOR_TILE_SN>,
      'stage' : <bare module stage>,
      'Vbd' : <VALUE>,
      'Vfd' : <VALUE>,
      'temperature' : <VALUE>,
      'IV_ARRAY' : { "time": [array], "voltage" : [ array ], "current" : [array], "sigma current": [array], "temperature": [array], "humidity": [array] }
    }
  ]
}
```
</details>

<details> <summary> analysis-IV-MEASURE --help </summary>

```
$ analysis-IV-MEASURE -h
Usage: analysis-IV-MEASURE [OPTIONS]
Options:
  -i, --input-meas PATH    path to the input measurement file or directory containing input measurement files. [default: None] [required]
  -o, --output-dir PATH           output directory  [default: outputs]
  -q, --qc-criteria PATH          path to reference IV measurement results from bare module stage. [default: None] [required]
  -l, --layer TEXT                Layer of module, used for applying correct
                                  QC criteria settings. Options: L0, L1, L2
                                  (default is automatically determined from module SN)
  -v, --verbosity [DEBUG|INFO|WARNING|ERROR]
                                  Log level [options: DEBUG, INFO (default)
                                  WARNING, ERROR]  [default: LogLevel.info]
      --site TEXT                 Your testing site. Required when submitting results. Please use same short-hand as on production DB, i.e. LBNL_PIXEL_MODULES for LBNL, IRFU for Paris-Saclay, ...
      --vdepl FLOAT               Depletion voltage [default: None]
```

</details>

### `ADC_CALIBRATION`

This analysis script performs the ADC calibration. It produces several
diagnostic plots and an output file with the ADC calibration slope and offset.

<details> <summary> analysis-ADC-CALIBRATION --help </summary>

```
analysis-ADC-CALIBRATION --help
usage: analysis-ADC-CALIBRATION [-h] -i INPUT_MEAS [-o OUTPUT_DIR] [-q QC_CRITERIA] [-l LAYER] [--permodule]
                                [-f {root,numpy}] [-v VERBOSITY]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_MEAS, --input-meas INPUT_MEAS
                        path to the input measurement file or directory containing input measurement files.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
  -q QC_CRITERIA, --qc-criteria QC_CRITERIA
                        path to json file with QC selection criteria (default: $(module-qc-analysis-tools --prefix)/analysis_cuts.json)
  -l LAYER, --layer LAYER
                        Layer of module, used for applying correct QC criteria settings. Default setting uses information from production database. Options: L0, L1, L2.
  --permodule           Store results in one file per module (default: one file per chip)
  -f {root,numpy}, --fit-method {root,numpy}
                        fitting method
  -v VERBOSITY, --verbosity VERBOSITY
                        Log level [options: DEBUG, INFO (default), WARNING, ERROR]
```

</details>

### `ANALOG_READBACK`

This analysis script performs the Analog Readback. It produces an output file
with the calculated internal biases, temperature from the internal and external
temperature sensor, and VDDA/VDDD vs Trim, including diagnostic plots with slope
and offset.

<details> <summary> analysis-ANALOG-READBACK --help </summary>

```
$ analysis-ANALOG-READBACK --help
usage: analysis-ANALOG-READBACK [-h] -i INPUT_MEAS [-o OUTPUT_DIR] [-q QC_CRITERIA] [-l LAYER] [--permodule]
                                [-f {root,numpy}] [-v VERBOSITY] [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_MEAS, --input-meas INPUT_MEAS
                        path to the input measurement file or directory containing input measurement files.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
  -q QC_CRITERIA, --qc-criteria QC_CRITERIA
                        path to json file with QC selection criteria (default: $(module-qc-analysis-tools --prefix)/analysis_cuts.json)
  -l LAYER, --layer LAYER
                        Layer of module, used for applying correct QC criteria settings. Default setting uses information from production database. Options: L0, L1, L2.
  --permodule           Store results in one file per module (default: one file per chip)
  -f {root,numpy}, --fit-method {root,numpy}
                        fitting method
  -v VERBOSITY, --verbosity VERBOSITY
                        Log level [options: DEBUG, INFO (default), WARNING, ERROR]
  --verbose             verbose mode

```

</details>

### `SLDO`

This script analyses the SLDO curve. It produces several diagnostic plots and an
output file with several parameters extracted from the SLDO curves.

<details> <summary> analysis-SLDO --help </summary>

```
$ analysis-SLDO --help
usage: analysis-SLDO [-h] -i INPUT_MEAS [-o OUTPUT_DIR] [-q QC_CRITERIA] [-l LAYER] [--permodule] [-n NCHIPS]
                     [-f {root,numpy}] [-v VERBOSITY] [--lp-enable]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_MEAS, --input-meas INPUT_MEAS
                        path to the input measurement file or directory containing input measurement files.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
  -q QC_CRITERIA, --qc-criteria QC_CRITERIA
                        path to json file with QC selection criteria (default: $(module-qc-analysis-tools --prefix)/analysis_cuts.json)
  -l LAYER, --layer LAYER
                        Layer of module, used for applying correct QC criteria settings. Default setting uses information from production database. Options: L0, L1, L2.
  --permodule           Store results in one file per module (default: one file per chip)
  -n NCHIPS, --nChips NCHIPS
                        Number of chips powered in parallel (e.g. 4 for a quad module, 3 for a triplet, 1 for an
                        SCC.)
  -f {root,numpy}, --fit-method {root,numpy}
                        fitting method
  -v VERBOSITY, --verbosity VERBOSITY
                        Log level [options: DEBUG, INFO (default), WARNING, ERROR]
  --lp-enable           low power mode

```

</details>

### `VCAL_CALIBRATION`

This analysis script performs the VCal calibration. It produces several
diagnostic plots and an output file with the VCal calibration slope and offset.

<details> <summary> analysis-VCAL-CALIBRATION --help </summary>

```
$ analysis-VCAL-CALIBRATION --help
usage: analysis-VCAL-CALIBRATION [-h] -i INPUT_MEAS [-o OUTPUT_DIR] [-q QC_CRITERIA] [-l LAYER] [--permodule]
                                 [-f {root,numpy}] [-v VERBOSITY]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_MEAS, --input-meas INPUT_MEAS
                        path to the input measurement file or directory containing input measurement files.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
  -q QC_CRITERIA, --qc-criteria QC_CRITERIA
                        path to json file with QC selection criteria (default: $(module-qc-analysis-tools --prefix)/analysis_cuts.json)
  -l LAYER, --layer LAYER
                        Layer of module, used for applying correct QC criteria settings. Default setting uses information from production database. Options: L0, L1, L2.
  --permodule           Store results in one file per module (default: one file per chip)
  -f {root,numpy}, --fit-method {root,numpy}
                        fitting method
  -v VERBOSITY, --verbosity VERBOSITY
                        Log level [options: DEBUG, INFO (default), WARNING, ERROR]
```

</details>

### `INJECTION_CAPACITANCE`

This analysis script performs the injection capacitance. It produces several
diagnostic plots and an output file with the measured pixel injection
capacitance.

<details> <summary> analysis-INJECTION-CAPACITANCE --help </summary>

```
$ analysis-INJECTION-CAPACITANCE --help
usage: analysis-INJECTION-CAPACITANCE [-h] -i INPUT_MEAS [-o OUTPUT_DIR] [-q QC_CRITERIA] [-l LAYER] [--permodule]
                                      [-v VERBOSITY]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_MEAS, --input-meas INPUT_MEAS
                        path to the input measurement file or directory containing input measurement files.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
  -q QC_CRITERIA, --qc-criteria QC_CRITERIA
                        path to json file with QC selection criteria (default: $(module-qc-analysis-tools --prefix)/analysis_cuts.json)
  -l LAYER, --layer LAYER
                        Layer of module, used for applying correct QC criteria settings. Default setting uses information from production database. Options: L0, L1, L2.
  --permodule           Store results in one file per module (default: one file per chip)
  -v VERBOSITY, --verbosity VERBOSITY
                        Log level [options: DEBUG, INFO (default), WARNING, ERROR]
```

</details>

### `LP_MODE`

This analysis script performs the Low Power mode analysis. It produces an output
file with the measured internal voltages and currents in low power mode.

<details> <summary> analysis-LP-MODE --help </summary>

```
$ analysis-LP-MODE --help
usage: analysis-LP-MODE [-h] -i INPUT_MEAS [-o OUTPUT_DIR] [-q QC_CRITERIA] [-l LAYER] [--permodule]
                                      [-v VERBOSITY]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_MEAS, --input-meas INPUT_MEAS
                        path to the input measurement file or directory containing input measurement files.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
  -q QC_CRITERIA, --qc-criteria QC_CRITERIA
                        path to json file with QC selection criteria (default: $(module-qc-analysis-tools --prefix)/analysis_cuts.json)
  -l LAYER, --layer LAYER
                        Layer of module, used for applying correct QC criteria settings. Default setting uses information from production database. Options: L0,
L1, L$
  --permodule           Store results in one file per module (default: one file per chip)
  -v VERBOSITY, --verbosity VERBOSITY
                        Log level [options: DEBUG, INFO (default), WARNING, ERROR]
```

</details>

### `OVERVOLTAGE_PROTECTION`

This analysis script performs the Overvoltage protection analysis. It produces
an output file with the measured internal voltages and currents in low power
mode and when overvoltage protection mechanism is activated.

<details> <summary> analysis-OVERVOLTAGE-PROTECTION --help </summary>

```
$ analysis-OVERVOLTAGE-PROTECTION --help
usage: analysis-OVERVOLTAGE-PROTECTION [-h] -i INPUT_MEAS [-o OUTPUT_DIR] [-q QC_CRITERIA] [-l LAYER] [--permodule]
                                      [-v VERBOSITY]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_MEAS, --input-meas INPUT_MEAS
                        path to the input measurement file or directory containing input measurement files.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
  -q QC_CRITERIA, --qc-criteria QC_CRITERIA
                        path to json file with QC selection criteria (default: $(module-qc-analysis-tools --prefix)/analysis_cuts.json)
  -l LAYER, --layer LAYER
                        Layer of module, used for applying correct QC criteria settings. Default setting uses information from production database. Options: L0,
L1, L$
  --permodule           Store results in one file per module (default: one file per chip)
  -v VERBOSITY, --verbosity VERBOSITY
                        Log level [options: DEBUG, INFO (default), WARNING, ERROR]
```

</details>

### `UNDERSHUNT_PROTECTION`

This analysis script performs the Undershunt protection analysis. It produces an
output file with the measured internal voltages and currents in when the
undershunt protection mechanism is activated.

<details> <summary> analysis-UNDERSHUNT-PROTECTION --help </summary>

```
$ analysis-UNDERSHUNT-PROTECTION --help
usage: analysis-UNDERSHUNT-PROTECTION [-h] -i INPUT_MEAS [-o OUTPUT_DIR] [-q QC_CRITERIA] [-l LAYER] [--permodule]
                                      [-v VERBOSITY]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_MEAS, --input-meas INPUT_MEAS
                        path to the input measurement file or directory containing input measurement files.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
  -q QC_CRITERIA, --qc-criteria QC_CRITERIA
                        path to json file with QC selection criteria (default: $(module-qc-analysis-tools
--prefix)/analysis_cuts.json)
  -l LAYER, --layer LAYER
                        Layer of module, used for applying correct QC criteria settings. Default setting uses
information from production database. Options: L0,
L1, L$
  --permodule           Store results in one file per module (default: one file per chip)
  -v VERBOSITY, --verbosity VERBOSITY
                        Log level [options: DEBUG, INFO (default), WARNING, ERROR]
```

</details>

### `DATA_TRANSMISSION`

This analysis script performs the data transmission. It produces several
diagnostic plots and an output file with the eye diagram width.

<details> <summary> analysis-DATA-TRANSMISSION --help </summary>

```
analysis-DATA-TRANSMISSION --help
usage: analysis-DATA-TRANSMISSION [-h] -i INPUT_MEAS [-o OUTPUT_DIR] [-q QC_CRITERIA] [-l LAYER] [--permodule]
                                [-v VERBOSITY]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_MEAS, --input-meas INPUT_MEAS
                        path to the input measurement file or directory containing input measurement files.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory
  -q QC_CRITERIA, --qc-criteria QC_CRITERIA
                        path to json file with QC selection criteria (default: $(module-qc-analysis-tools --prefix)/analysis_cuts.json)
  -l LAYER, --layer LAYER
                        Layer of module, used for applying correct QC criteria settings. Default setting uses information from production database. Options: L0, L1, L2.
  --permodule           Store results in one file per module (default: one file per chip)
  -v VERBOSITY, --verbosity VERBOSITY
                        Log level [options: DEBUG, INFO (default), WARNING, ERROR]
```

</details>

### `MIN_HEALTH_TEST`

This analysis script performs the minimum health analysis of YARR Scans. It
produces an output file with key parameters (number of dead/bad pixels, ...).
Note that the YARR scans to be used in the analysis should be identified with
`analysis-load-yarr-scans`, see [Load Yarr Scans](#load-yarr-scans).

<details> <summary> analysis-MIN_HEALTH_TEST --help </summary>

```
$ analysis-MIN-HEALTH-TEST -h
Usage: analysis-MIN-HEALTH-TEST [OPTIONS]

Options:
  -i, --input-yarr-config PATH    path to the json config file containing
                                  paths to YARR scan outputs. Run analysis-
                                  load-yarr-scans.py to generate.  [default:
                                  info.json]
  -q, --qc-criteria PATH          path to json file with QC selection criteria
                                  [default: /home/eathompson/module-qc-
                                  analysis-tools/src/module_qc_analysis_tools/
                                  data/analysis_cuts.json]
  -p, --pixel-failure-config PATH
                                  path to json file with pixel failure
                                  selection criteria  [default:
                                  /home/eathompson/module-qc-analysis-tools/sr
                                  c/module_qc_analysis_tools/data/pixel_classi
                                  fication.json]
  -l, --layer TEXT                Layer of module, used for applying correct
                                  QC criteria settings. Options: L0, L1, L2
                                  (default is automatically determined from module SN)
  -o, --output-dir PATH           output directory  [default: outputs]
  --permodule / --no-permodule    Store results in one file per module
                                  (default: one file per chip)  [default: no-
                                  permodule]
  -v, --verbosity [DEBUG|INFO|WARNING|ERROR]
                                  Log level [options: DEBUG, INFO (default)
                                  WARNING, ERROR]  [default: LogLevel.info]
```

</details>

### `TUNING`

This analysis script analyzes the tuning performance from YARR scans. It
produces an output file with key parameters (threshold before/after tuning,
...). Note that the YARR scans to be used in the analysis should be identified
with `analysis-load-yarr-scans`, see [Load Yarr Scans](#load-yarr-scans).

<details> <summary> analysis-TUNING --help </summary>

```
$ analysis-TUNING -h
Usage: analysis-TUNING [OPTIONS]

Options:
  -i, --input-yarr-config PATH    path to the json config file containing
                                  paths to YARR scan outputs. Run analysis-
                                  load-yarr-scans.py to generate.  [default:
                                  info.json]
  -q, --qc-criteria PATH          path to json file with QC selection criteria
                                  [default: /home/eathompson/module-qc-
                                  analysis-tools/src/module_qc_analysis_tools/
                                  data/analysis_cuts.json]
  -p, --pixel-failure-config PATH
                                  path to json file with pixel failure
                                  selection criteria  [default:
                                  /home/eathompson/module-qc-analysis-tools/sr
                                  c/module_qc_analysis_tools/data/pixel_classi
                                  fication.json]
  -l, --layer TEXT                Layer of module, used for applying correct
                                  QC criteria settings. Options: L0, L1, L2
                                  (default is automatically determined from module SN)
  -o, --output-dir PATH           output directory  [default: outputs]
  --permodule / --no-permodule    Store results in one file per module
                                  (default: one file per chip)  [default: no-
                                  permodule]
  -v, --verbosity [DEBUG|INFO|WARNING|ERROR]
                                  Log level [options: DEBUG, INFO (default)
                                  WARNING, ERROR]  [default: LogLevel.info]
```

</details>

### `PIXEL_FAILURE_ANALYSIS`

This analysis script classifies pixel failures and performs the pixel failure
analysis. It produces an output file with several key parameters (number of
pixels failing each category, total failing pixels, ...). Note that the YARR
scans to be used in the analysis should be identified with
`analysis-load-yarr-scans`, see [Load Yarr Scans](#load-yarr-scans).

<details> <summary> analysis-PIXEL-FAILURE-ANALYSIS --help </summary>

```
$ analysis-PIXEL-FAILURE-ANALYSIS -h
Usage: analysis-PIXEL-FAILURE-ANALYSIS [OPTIONS]

Options:
  -i, --input-yarr-config PATH    path to the json config file containing
                                  paths to YARR scan outputs. Run analysis-
                                  load-yarr-scans.py to generate.  [default:
                                  info.json]
  -q, --qc-criteria PATH          path to json file with QC selection criteria
                                  [default: /home/eathompson/module-qc-
                                  analysis-tools/src/module_qc_analysis_tools/
                                  data/analysis_cuts.json]
  -p, --pixel-failure-config PATH
                                  path to json file with pixel failure
                                  selection criteria  [default:
                                  /home/eathompson/module-qc-analysis-tools/sr
                                  c/module_qc_analysis_tools/data/pixel_classi
                                  fication.json]
  -l, --layer TEXT                Layer of module, used for applying correct
                                  QC criteria settings. Options: L0, L1, L2
                                  (default is automatically determined from module SN)
  -o, --output-dir PATH           output directory  [default: outputs]
  --permodule / --no-permodule    Store results in one file per module
                                  (default: one file per chip)  [default: no-
                                  permodule]
  -v, --verbosity [DEBUG|INFO|WARNING|ERROR]
                                  Log level [options: DEBUG, INFO (default)
                                  WARNING, ERROR]  [default: LogLevel.info]

```

</details>

## Notes

### `Submit QC results`

To submit the QC results, supply the --submit option to the analysis. You also
need to supply the site where the testing took place, as written in production
DB (i.e. LBNL_PIXEL_MODULES for LBNL, IRFU for Paris-Saclay, ...). This will
generate a URL that is printed to the terminal and saved in "submit.txt" in the
same folder as the analysis output. To submit the results, you need to copy and
paste one URL for each chip / test into a browser. Once submitted, the results
can be viewed here:
https://docs.google.com/spreadsheets/d/1pw_07F94fg2GJQr8wlvhaRUV63uhsAuBt_S1FEFBzBU/view
. While all submitted results will be recorded, only the latest results for each
chip / test will be analyzed. If a mistake was realized in the submitted
results, one can re-run the analysis and re-submit the results to overwrite the
original results.

### `Example commands for a chip in a quad module`

```
analysis-ADC-CALIBRATION -i ../module-qc-tools/emulator/outputs/Measurements/ADC_CALIBRATION/1000000001/
analysis-SLDO -i ../module-qc-tools/emulator/outputs/Measurements/SLDO/1000000001/
analysis-ANALOG-READBACK -i ../module-qc-tools/emulator/outputs/Measurements/ANALOG_READBACK/1000000001/
analysis-VCAL-CALIBRATION -i ../module-qc-tools/emulator/outputs/Measurements/VCAL_CALIBRATION/1000000001/
analysis-INJECTION-CAPACITANCE -i ../module-qc-tools/emulator/outputs/Measurements/INJECTION_CAPACITANCE/1000000001/
```

### `Update Chip Config`

After each analysis, update the settings in the chip config by running:

```
analysis-update-chip-config -i <path to analysis output directory> -c <path to YARR config directory> -t <config type>
```

This script reads the analysis test type and update the corresponding parameters
in the chip config.

<details> <summary> analysis-update-chip-config --help </summary>

```
analysis-update-chip-config -h

-i,  --input-dir                              Analysis output directory [default: None] [required]
-c,  --config-dir                             Path to the module configuration directory to be modified [default: None] [required]
-t,  --config-type                            The config type to be modified. E.g. L2_warm/L2_cold.
     --override/--no-override                 Update chip configuration even if the chip failed QC [default: no-override]
     --install-completion                     Install completion for the current shell.
     --show-completion                        Show completion for the current shell, to copy it or customize the installation.
-h,  --help                                   Show this message and exit.
```

</details>

### `Load YARR Scans`

Before running analysis of YARR scans (`MIN_HEALTH_TEST`, `TUNING`,
`PIXEL_FAILURE_ANALYSIS`), the YARR scans to be analyzed need to be identified.
This is done locally using the following script:

<details> <summary> analysis-load-yarr-scans --help </summary>

```
$ analysis-load-yarr-scans -h
Options:
  -o, --output-yarr PATH          output directory to put
                                  info_{TEST_NAME}.json which will be used as
                                  input to YARR scan analysis  [default: ./]
  -m, --moduleSN TEXT             Module serial number  [required]
  -v, --verbosity [DEBUG|INFO|WARNING|ERROR]
                                  Log level [options: DEBUG, INFO (default)
                                  WARNING, ERROR]  [default: LogLevel.info]
  -t, --test-name TEXT            Test name (MIN_HEALTH_TEST, TUNING, or
                                  PIXEL_FAILURE_ANALYSIS)  [required]
  -ds, --digital-scan PATH        path to the digital scan output directory to
                                  use in YARR analysis
  -as, --analog-scan PATH         path to the analog scan output directory to
                                  use in YARR analysis
  -hr, --threshold-scan-hr PATH   path to the threshold scan (high-range)
                                  output directory to use in YARR analysis
  -hd, --threshold-scan-hd PATH   path to the threshold scan (high-def) output
                                  directory to use in YARR analysis
  -ns, --noise-scan PATH          path to the noise scan output directory to
                                  use in YARR analysis
  -zb, --zerobias PATH            path to the threshold scan (high-def, zero-
                                  bias) output directory to use in YARR
                                  analysis
  -db, --discbump PATH            path to the disconnected bump scan output
                                  directory to use in YARR analysis
```

</details>

Given a directory with YARR scans, the script will identify the latest YARR
scans needed for all analyses. Alternatively, the paths to YARR scans for each
type of scan can be supplied to the script.

## For Developer

### python version

A python version higher than 3.7 is needed for this repository. Check the local
python version with `python -V`.

If the local python version is lower, set up a virtual python environment
following the instructions
[here](https://itk.docs.cern.ch/general/Virtual_Environments/).

### versioning

In case you need to tag the version of the code, you need to have either `hatch`
or `pipx` installed.

1. Activate python environment, e.g. `source venv/bin/activate`.
2. Run `python -m pip install hatch` or `python -m pip install pipx`.

You can bump the version via:

```
pipx run hatch run tag x.y.z

# or

hatch run tag x.y.z
```

where `x.y.z` is the new version to use. This should be run from the default
branch (`main` / `master`) as this will create a commit and tag, and push for
you. So make sure you have the ability to push directly to the default branch.

### pre-commit

Install pre-commit to avoid CI failure. Once pre-commit is installed, a git hook
script will be run to identify simple issues before submission to code review.

Instruction for installing pre-commit in a python environment:

1. Activate python environment, e.g. `source venv/bin/activate`.
2. Run `python3 -m pip install pre-commit`.
3. Run `pre-commit install` to install the hooks in `.pre-commit-config.yaml`.

After installing pre-commit, `.pre-commit-config.yaml` will be run every time
`git commit` is done. Redo `git add` and `git commit`, if the pre-commit script
changes any files.
