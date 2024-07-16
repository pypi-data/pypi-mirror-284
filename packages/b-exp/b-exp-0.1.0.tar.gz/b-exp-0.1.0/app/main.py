from .utils import load_document, extract_client_from_path, extract_data, save_to_csv, get_file_paths
import click
import os
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

@click.command()
@click.pass_context
def extract(ctx):
    """
    Extract data from multiple Word documents and save it to a single CSV file.
    """
    try:
        input_docxs, output_csv = get_file_paths()
        failed_csv = os.path.splitext(output_csv)[0] + "_failed.csv"

        aggregated_data = {
            'collections': [],
            'type': [],
            'name': [],
            'notes': [],
            'fields': [],
            'reprompt': [],
            'login_uri': [],
            'login_username': [],
            'login_password': [],
            'login_totp': []
        }

        failed_data = {
            'collections': [],
            'type': [],
            'name': [],
            'notes': [],
            'fields': [],
            'reprompt': [],
            'login_uri': [],
            'login_username': [],
            'login_password': [],
            'login_totp': []
        }

        for input_docx in input_docxs:
            logging.debug(f"Processing file: {input_docx}")
            root = extract_client_from_path(input_docx)
            if not root:
                logging.error(f"Client not found in file path: {input_docx}")
                continue

            try:
                doc = load_document(input_docx)
                computer_name, local_admin_username, local_admin_password, errors, complete_data = extract_data(doc)

                if computer_name and local_admin_username and local_admin_password and computer_name != "Follow client naming convention":
                    aggregated_data['collections'].append('Clients/' + root + '/Client Builds')
                    aggregated_data['type'].append('login')
                    aggregated_data['name'].append(computer_name)
                    aggregated_data['notes'].append('')
                    aggregated_data['fields'].append('')
                    aggregated_data['reprompt'].append('')
                    aggregated_data['login_uri'].append('')
                    aggregated_data['login_username'].append(local_admin_username)
                    aggregated_data['login_password'].append(local_admin_password)
                    aggregated_data['login_totp'].append('')
                else:
                    failed_data['collections'].append('Clients/' + root + '/Client Builds')
                    failed_data['type'].append('login')
                    failed_data['name'].append(os.path.basename(input_docx))
                    failed_data['notes'].append('')
                    failed_data['fields'].append('')
                    failed_data['reprompt'].append('')
                    failed_data['login_uri'].append('')
                    failed_data['login_username'].append(complete_data)
                    failed_data['login_password'].append('')
                    failed_data['login_totp'].append('')

                if errors:
                    for error in errors:
                        logging.error(f"Error in document {input_docx}: {error}")

            except Exception as e:
                logging.exception(f"Error processing document {input_docx}: {e}")

        save_to_csv(aggregated_data, output_csv)
        save_to_csv(failed_data, failed_csv)
        logging.info(f"Data has been successfully extracted and saved to {output_csv}")
        logging.info(f"Failed extractions have been saved to {failed_csv}")

    except ValueError as ve:
        logging.info(f"{ve}")
        click.echo(f"{ve}")
        ctx.invoke(menu)

    except Exception as e:
        logging.exception(f"An error occurred: {e}")


@click.command()
@click.pass_context
def menu(ctx):
    """
    Display a menu for selecting actions.
    """
    while True:
        print("1. Extract data from Word documents")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ctx.invoke(extract)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
