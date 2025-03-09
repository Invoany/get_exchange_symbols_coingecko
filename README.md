## How to Get All Exchange Symbols Using the Script

This Python script retrieves information about all cryptocurrency exchanges identified by [CoinGecko](https://www.coingecko.com/en). It saves the data as a CSV file and logs the number of records written to enhance traceability.

### Features
- **Error Handling**: Handles API and file-related errors gracefully.
- **Retry Mechanism**: Automatically retries API requests in case of network or server issues.
- **Configurable Parameters**: Allows customization of the output folder and file-saving behavior.
- **Logging**: Logs key events, errors, and details about the number of rows written in the output CSV.
- **Config File**: Supports external configuration for settings like the API base URL.

---

### How It Works

1. **API Request**: 
   The script uses the `requests` library to query the CoinGecko `/exchanges/list` endpoint. A retry mechanism ensures resilience to network interruptions.

   ```python
   session = requests_retry_session()
   response = session.get(base_url + "exchanges/list")
   response.raise_for_status()
   ```

2. **Data Transformation**: 
   The API response is validated and transformed into a pandas DataFrame, which organizes the data into a tabular format.

   ```python
   df_exchange_symbols = pd.DataFrame(exchange_data)
   ```

3. **Saving Data**: 
   The script saves the processed data as a CSV file in a specified output directory, using a filename that includes the current date. It also logs how many rows were written and the file path.

   ```python
   file_path = os.path.join(output_folder, f"AllExchanges_{current_date()}.csv")
   df.to_csv(file_path, index=False)
   logging.info(f"Written {len(df)} lines to CSV: {file_path}")
   ```

4. **Logging**: 
   Logs provide details of the script's operation and any encountered issues. Logs are saved in a file (`exchange.log`) and include timestamps with millisecond precision.

---

### Directory Structure

The following directory structure is recommended for running the script:

```plaintext
project_folder/
├── config/
│   ├── config.json
├── Output/  # Automatically created if missing
├── exchange.log
├── main.py
├── controller/
│   ├── exchange_controller.py
├── model/
│   ├── exchange_model.py
│   ├── data_treatment.py
├── view/
│   ├── exchange_view.py
```

---

### Example `config.json`

The script reads configuration settings such as the API base URL from a `config/config.json` file. Below is an example:

```json
{
    "base_url": "https://api.coingecko.com/api/v3/"
}
```

If the file is missing, default settings are used.

---

### Installation and Dependencies

Install the required Python libraries before running the script:

```bash
pip install requests pandas
```

---

### Running the Script

1. Clone or download the repository.
2. Navigate to the script's directory.
3. Run the script:

   ```bash
   python main.py
   ```

---

### Output

The script creates a CSV file in the output folder (default: `Output`) with the following naming convention:

`AllExchanges_YYYYMMDD.csv`

The CSV file contains:
- Exchange ID
- Exchange Name
- Additional metadata provided by CoinGecko.

Additionally, the log file (`exchange.log`) records how many rows were written and the exact file path.

---

### Features in Detail

- **Error Handling**: Catches errors related to API requests or file saving, ensuring robust operation.
- **Retry Mechanism**: Automatically retries API requests for a configurable number of attempts to handle transient failures.
- **Logging**: Logs key actions, including the creation of output directories, successful API calls, file-saving operations, and the number of records written.
- **Customizable Output**: Allows you to specify the output folder or disable file-saving entirely, making the function flexible for different use cases.

---

### Notes

- Ensure your system has internet access to retrieve data from the CoinGecko API.
- If no custom output folder is provided, the script uses a default folder named `Output`.
- The logging system records timestamps with millisecond precision for improved debugging.

This script is an efficient way to retrieve and save exchange data for cryptocurrency analysis or integration into broader projects. 🚀