import os
import glob
import pandas as pd

def compile_csvs():
    output_filename = "compiled_data_output.csv"
    csv_files = [f for f in glob.glob("*.csv") if f != output_filename]
    
    if not csv_files:
        print("No CSV files found in the current directory.")
        return

    print(f"Found {len(csv_files)} CSV files. Compiling...")
    
    df_list = []
    
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            
            df['Source_File'] = file
            
            df_list.append(df)
            print(f" - Added: {file}")
        except Exception as e:
            print(f" - Error reading {file}: {e}")

    if df_list:
        combined_df = pd.concat(df_list, ignore_index=True)
        
        combined_df.to_csv(output_filename, index=False)
        
        print(f"\nSuccess! Compiled data saved to '{output_filename}'.")
    else:
        print("\nNo data was compiled.")

if __name__ == "__main__":
    compile_csvs()
    input("\nPress Enter to exit...")
