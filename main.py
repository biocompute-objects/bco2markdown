import json
import mdutils
import datetime


def format_time(time_input):
    spliced = time_input[0:10]
    try:
        date = datetime.date.fromisoformat(spliced)
        return date.strftime("%A %d, %B %Y")
    except ValueError:
        date = spliced
        return date


def table_create(md_file, data, headers, values):
    columns = len(headers)
    for i in range(len(data)):
        for j in range(len(values)):
            try:
                if type(data[i][values[j]]) == list:
                    headers.append(', '.join(data[i][values[j]]))
                elif values[j] == 'access_time':
                    headers.append(format_time(data[i][values[j]]))
                else:
                    headers.append(data[i][values[j]])
            except KeyError:
                headers.append('N/A')
    md_file.new_line()
    md_file.new_table(columns, len(data) + 1, headers, text_align='center')


def read_object_id(data, md_file):
    md_file.new_line("Object ID: " + data)


def read_spec_version(data, md_file):
    md_file.new_line("Spec Version: " + data)


def read_etag(data, md_file):
    md_file.new_line("etag: " + data)


def read_provenance(data, md_file):
    md_file.new_header(level=1, title='Provenance')
    md_file.new_line("Version: " + data['version'])
    md_file.new_line("License: " + data['license'])
    md_file.new_line("Created: " + data['created'])
    md_file.new_line("Modified: " + data['modified'])
    try:
        if data['embargo'] != {}:
            md_file.new_line("Embargo: " + data['embargo'])
    except KeyError:
        pass

    md_file.new_line()
    md_file.new_header(level=3, title='Contributors')
    contributers = data['contributors']
    contributers_attributes = ["Name", "Contribution", "Affiliation", "Email", "ORCID"]
    contributer_values = ['name', 'contribution', 'affiliation', 'email', 'orcid']
    table_create(md_file, contributers, contributers_attributes, contributer_values)

    md_file.new_line()
    md_file.new_header(level=3, title='Review')
    review = data['review']
    review_attributes = ["Name",
                         "Contribution",
                         "Affiliation",
                         "Email",
                         "ORCID",
                         "Status",
                         "Comments",
                         "Date"]
    review_values = ['name', 'contribution', 'affiliation', 'email', 'orcid', 'status', 'reviewer_comment', 'date']
    for i in range(len(review)):
        for j in range(len(review_values)):
            try:
                try:
                    review_attributes.append(review[i]['reviewer'][review_values[j]])
                except KeyError:
                    if review_values[j] == "date":
                        review_attributes.append(format_time(review[i][review_values[j]]))
                    else:
                        review_attributes.append(review[i][review_values[j]])
            except KeyError:
                review_attributes.append("N/A")
    md_file.new_line()
    md_file.new_table(columns=8,
                      rows=len(review) + 1,
                      text=review_attributes,
                      text_align='center')


def read_usability(data, md_file):
    md_file.new_header(level=1, title='Usability')
    for i in range(len(data)):
        md_file.new_line(data[i])


def read_description(data, md_file):
    md_file.new_header(level=1, title='Description')

    md_file.new_header(level=2, title='Keywords')
    md_file.new_line(', '.join(data['keywords']))

    md_file.new_header(level=2, title='External References')
    xref_attributes = ["Name", "Namespace", "Access Time", "IDs"]
    xref = data['xref']
    for i in range(len(xref)):
        xref_attributes.extend([xref[i]['name'],
                                xref[i]['namespace'],
                                format_time(xref[i]['access_time']),
                                ', '.join(xref[i]['ids'])])
    md_file.new_line()
    md_file.new_table(columns=4,
                      rows=len(xref) + 1,
                      text=xref_attributes,
                      text_align='center')

    md_file.new_header(level=2, title="Platform")
    md_file.new_line(', '.join(data['platform']))

    md_file.new_header(level=2, title="Pipeline Steps")
    steps = data['pipeline_steps']
    for i in range(len(steps)):
        md_file.new_line("Step " + str(steps[i]['step_number']) + ": " + steps[i]['name'], bold_italics_code='bi')
        md_file.new_line("Version: " + steps[i]['version'])
        md_file.new_line("Description: " + steps[i]['description'])
        try:
            prereq = steps[i]['prerequisite']
            md_file.new_line("Prerequisites", bold_italics_code='b')
            prereq_att = ['Name', 'uri', 'Access time']
            for j in range(len(prereq)):
                prereq_att.extend([prereq[j]["name"],
                                   prereq[j]['uri']['uri'],
                                   format_time(prereq[j]['uri']['access_time'])])
            md_file.new_line()
            md_file.new_table(columns=3, rows=len(prereq) + 1, text=prereq_att, text_align='center')
        except KeyError:
            pass
        md_file.new_line("Input List", bold_italics_code='b')
        table_create(md_file, steps[i]['input_list'], ['Name', 'uri', 'Access Time'], ['name', 'uri', 'access_time'])
        md_file.new_line("Output List", bold_italics_code='b')
        table_create(md_file, steps[i]['output_list'], ['Name', 'uri', 'Access Time'], ['name', 'uri', 'access_time'])


def read_parametric(data, md_file):
    md_file.new_header(level=1, title="Parametric Domain")
    param_att = ["Parameter", "Step", "Value"]
    param_values = ['param', 'step', 'value']
    table_create(md_file, data, param_att, param_values)


def read_io(data, md_file):
    md_file.new_header(level=1, title="IO Domain")

    md_file.new_header(level=2, title="Input Subdomain")
    inputs = data['input_subdomain']
    input_att = ['Filename', 'URI', 'Access Time', 'SHA Checksum']
    input_values = ['filename', 'uri', 'access_time', 'sha1_checksum']
    for i in range(len(inputs)):
        for j in range(len(input_values)):
            try:
                if input_values[j] == 'access_time':
                    input_att.append(format_time(inputs[i]["uri"][input_values[j]]))
                else:
                    input_att.append(inputs[i]["uri"][input_values[j]])
            except KeyError:
                input_att.append('N/A')
    md_file.new_line()
    md_file.new_table(4, len(inputs) + 1, input_att, text_align='center')

    md_file.new_header(level=2, title="Output Subdomain")
    output = data['output_subdomain']
    output_att = ['Media type', 'Filename', 'URI', 'Access Time', 'SHA Checksum']
    output_values = ['mediatype', 'filename', 'uri', 'access_time', 'sha1_checksum']
    for i in range(len(output)):
        for j in range(len(output_values)):
            try:
                try:
                    if output_values[j] == 'access_time':
                        output_att.append(format_time(output[i]["uri"][output_values[j]]))
                    else:
                        output_att.append(output[i]["uri"][output_values[j]])
                except KeyError:
                    output_att.append(output[i][output_values[j]])
            except KeyError:
                output_att.append("N/A")
    md_file.new_line()
    md_file.new_table(5, len(output) + 1, output_att, text_align='center')


def read_execution(data, md_file):
    md_file.new_header(level=1, title="Execution Domain")
    md_file.new_line("Script Driver: " + data['script_driver'])

    md_file.new_header(level=2, title="Scripts:")
    script = data['script']
    script_att = ["Filename", "URI", "Access Time"]
    script_values = ['filename', 'uri', 'access_time']
    for i in range(len(script)):
        for j in range(len(script_values)):
            try:
                if script_values[j] == "access_time":
                    script_att.append(format_time(script[i]['uri'][script_values[j]]))
                else:
                    script_att.append(script[i]['uri'][script_values[j]])
            except KeyError:
                script_att.append("N/A")
    md_file.new_line()
    md_file.new_table(3, len(script) + 1, script_att, text_align='center')

    md_file.new_header(level=2, title="Environment Variables")
    for i in data["environment_variables"].keys():
        md_file.new_line(i + ": " + data["environment_variables"][i])

    md_file.new_header(level=2, title="Software Prerequisites")
    soft = data['software_prerequisites']
    soft_att = ["Name", "Version", "URI", "Access Time", "SHA Checksum"]
    soft_val = ['name', 'version', 'uri', 'access_time', 'sha1_checksum']
    for i in range(len(soft)):
        for j in range(len(soft_val)):
            try:
                try:
                    if soft_val[j] == "access_time":
                        soft_att.append(format_time(soft[i]["uri"][soft_val[j]]))
                    else:
                        soft_att.append(soft[i]["uri"][soft_val[j]])
                except KeyError:
                    soft_att.append(soft[i][soft_val[j]])
            except KeyError:
                soft_att.append("N/A")
    md_file.new_line()
    md_file.new_table(5, len(soft) + 1, soft_att, text_align='center')

    md_file.new_header(level=2, title="External Data Endpoints")
    ede = data['external_data_endpoints']
    ede_att = ["Name", "URL"]
    ede_val = ['name', 'url']
    table_create(md_file, ede, ede_att, ede_val)


def read_error(data, md_file):
    md_file.new_header(level=1, title="Error Domain")
    for i in data.keys():
        md_file.new_header(level=2, title=i)
        for j in data[i].keys():
            md_file.new_line(j + ": " + data[i][j])


def create_markdown(jsonfile):
    file = open(jsonfile)
    data = json.load(file)
    md_file = mdutils.MdUtils(file_name=jsonfile[:-5])

    md_file.new_header(level=1, title=data['provenance_domain']['name'])

    try:
        read_object_id(data['object_id'], md_file)
    except KeyError:
        pass
    try:
        read_spec_version(data['spec_version'], md_file)
    except KeyError:
        pass
    try:
        read_etag(data['etag'], md_file)
    except KeyError:
        pass
    try:
        read_usability(data['usability_domain'], md_file)
    except KeyError:
        pass
    try:
        read_description(data['description_domain'], md_file)
    except KeyError:
        pass
    try:
        read_parametric(data['parametric_domain'], md_file)
    except KeyError:
        pass
    try:
        read_io(data['io_domain'], md_file)
    except KeyError:
        pass
    try:
        read_execution(data['execution_domain'], md_file)
    except KeyError:
        pass
    try:
        read_error(data['error_domain'], md_file)
    except KeyError:
        pass
    try:
        read_provenance(data['provenance_domain'], md_file)
    except KeyError:
        pass

    md_file.create_md_file()
    file.close()


create_markdown('deepprog.json')
