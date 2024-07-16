# How to use

## Clone code and change directory

```
    git clone git@gitlab.com:bechtle-cisco-devnet/netbox/netboxninja.git
    cd netboxninja
```

## Create and load a venv (linux/mac)
```
    python -m venv venv
    source venv/bin/activate
```

## Install the requirements
```
    pip install -r requirements.txt
```

## The .env File

Rename the dotenv file to .env.
Open the .env file and fill in your information.

## Start the Tool
```
    python -m netboxNinja --csv <path-to-your-csv>
```
