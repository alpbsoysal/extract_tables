#########################################
############## USER INPUTS ##############
#########################################
############## MAIN INPUTS ##############
#########################################

# IMPORTANT NOTE: IT IS ASSUMED THAT THE BATCH NUMBERS WILL KEEP INCREASING
# EVEN AFTER THE CYCLE CHANGES! THIS IS VITAL FOR THE REMAINING WORKFLOW!
# THE BATCH NUMBERS MUST BE UNIQUE!!!
batch_number = 1
cycle = 'Nov'

# Location of the PDF files
path_to_pdfs = 'testing/everything/pdfs'

# Location of the mapping file
path_to_mapping = 'testing/everything/pdfs'
# Name of mapping file
mapping_name = 'mapping.xlsx'

# Path to banner file
path_to_banner = 'testing/everything/pdfs'
# Name of banner file
banner_name = 'Batch 1.xlsx'

# Path to database CSV
path_to_database = 'testing/everything/data'
# Name of database CSV
database_name = 'previously_extracted.csv'

# Path to output directory
output_path = 'testing/everything/output'

#########################################
############ AUXILIARY INPUTS ###########
#########################################

# Keys are the initials of markers, values are the weighting of applications to be allocated
# to that person.
allocation_details = {
    "AP": 1,
    "TM": 1,
    "EN": 1,
}

# _ is used as a delimeter to split the filename of the pdf
# This index is for which item in the list (from split) corresponds to the
# ID of an applicant
pdf_filename_split_delimeter = "_"
pdf_filename_split_index = 2

# Sheet name of the qualification mapping in mapping file
qualification_mapping_sheet_name = "Mapping"

is_id_file_banner = True
is_banner_cumulative = True
# Column in banner file that contains IDs
which_column = "F"

database_headers = ["ID No.", "Batch No.", "Timestamp"]
database_header_id_num_index = 0
database_header_batch_index = 1
database_header_timestamp_index = 2

terminate_if_batch_num_repeated = True

#########################################
############# END OF INPUTS #############
#########################################

import os

def get_full_file_path(path, filename):
    """Combines path and filename to return full abs path as raw string"""
    return (
        os.path.abspath(os.path.join(path, filename)).encode("unicode-escape").decode()
    )


def get_full_path(path):
    """Combines path and filename to return full abs path as raw string"""
    return os.path.abspath(path).encode("unicode-escape").decode()


path_to_pdfs_to_extract = get_full_path(path_to_pdfs)

path_to_mapping_file = get_full_file_path(path_to_mapping, mapping_name)

path_to_target_file = get_full_file_path(path_to_banner, banner_name)

assert (
    max(
        database_header_id_num_index,
        database_header_batch_index,
        database_header_timestamp_index,
    )
    < len(database_headers)
)

path_to_database_of_extracted_pdfs = get_full_file_path(path_to_database, database_name)

output_path = get_full_path(output_path)

path_to_pdf_pool = os.path.join(output_path, "pool")
path_to_pdf_pool = get_full_path(path_to_pdf_pool)

if not os.path.exists(path_to_pdf_pool):
    os.makedirs(path_to_pdf_pool)

output_filename = f"grades_{batch_number}.xlsx"

log_filename = f"execution_log_{batch_number}.log"
path_to_log = get_full_file_path(output_path, log_filename)
ids_in_folder_file = f"id_log_{batch_number}.txt"
path_to_folder_ids = get_full_file_path(output_path, ids_in_folder_file)
