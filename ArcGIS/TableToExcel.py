# Name: TableToExcel_2.py
import arcpy
# Set environment settings
arcpy.env.workspace = "d:/Documents/GitHub/MCM2021_C"
# Set local variables
in_table = "ProblemC.gdb/Elevation_original_table"
out_xlsx = "elevations.xlsx"
# Execute TableToExcel
arcpy.TableToExcel_conversion(in_table, out_xlsx)