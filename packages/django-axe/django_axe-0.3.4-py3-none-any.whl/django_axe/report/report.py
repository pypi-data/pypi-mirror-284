import json
import logging
import os
from django.template.loader import render_to_string
from functools import wraps

logger = logging.getLogger(name="django_axe").setLevel(logging.INFO)

SAMPLE_REPORT = {
    "testEngine": {},
    "testRunner": {},
    "testEnvironment": [],
    "timestamp": "",
    "url": "",
    "toolOptions": {},
    "inapplicable": [],
    "passes": [],
    "incomplete": [],
    "violations": [],
}


def get_wcag_reference(tags):
    """
    Returns the WCAG reference(s) based on the given tags.

    Args:
        tags (list): A list of tags.

    Returns:
        str: The WCAG reference(s) as a string.

    """
    if "best-practice" in tags:
        return "Best practice"
    found_wcag_tags = [tag for tag in tags if "wcag" in tag]
    if found_wcag_tags:
        return ", ".join(found_wcag_tags)
    return ", ".join(tags)


def simplify_axe_result_for_summary(results):
    """
    Simplifies the Axe results for summary.

    This function takes a list of Axe results and simplifies each result by adding additional information such as index,
    WCAG reference, and impact. The simplified results are then appended to a summary list.

    Args:
        results (list): A list of Axe results.

    Returns:
        list: A list of simplified Axe results for summary.

    """
    summary = []
    for result_index, result in enumerate(results):
        result["index"] = result_index + 1
        result["wcag"] = get_wcag_reference(result["tags"])
        result["impact"] = result["impact"] or "n/a"
        summary.append(result)
    return summary


def prepare_fix_summary(failure_summary, default_highlight):
    """
    Prepare fix summaries for a given failure summary.

    Args:
        failure_summary (str): The failure summary to be processed.
        default_highlight (str): The default highlight to be used when a fix summary is empty.

    Returns:
        list: A list of fix summaries, where each fix summary is a dictionary with a "highlight" key and a "list" key.
              The "highlight" key contains the highlight for the fix summary, and the "list" key contains the list of
              lines for the fix summary.

    """
    fix_summaries = []
    failure_summaries_split = failure_summary.split("\n\n")
    for summary in failure_summaries_split:
        fix_summary_split = summary.split("\n")
        if len(fix_summary_split) == 0:
            fix_summaries.append(default_highlight)
        else:
            highlight = fix_summary_split.pop(0)
            fix_summaries.append({"highlight": highlight, "list": fix_summary_split})
    return fix_summaries


def prepare_report_data(violations, passes=None, incomplete=None, inapplicable=None):
    """
    Prepare the data for generating a report based on the accessibility violations.

    Args:
        violations (list): A list of accessibility violations.
        passes (list, optional): A list of passed checks. Defaults to None.
        incomplete (list, optional): A list of incomplete checks. Defaults to None.
        inapplicable (list, optional): A list of inapplicable checks. Defaults to None.

    Returns:
        dict: A dictionary containing the prepared report data.

    """
    passed_checks = simplify_axe_result_for_summary(passes) if passes else None
    incomplete_checks = (
        simplify_axe_result_for_summary(incomplete) if incomplete else None
    )
    inapplicable_checks = (
        simplify_axe_result_for_summary(inapplicable) if inapplicable else None
    )
    violations_total = sum(len(result["nodes"]) for result in violations)
    if len(violations) == 0:
        return {
            "violations_summary": 'Accessability scanner found <span class="py-1 px-3 text-center font-semibold text-slate-100 rounded bg-green-600">0</span> violations',
            "checks_passed": passed_checks,
            "checks_incomplete": incomplete_checks,
            "checks_inapplicable": inapplicable_checks,
        }
    violations_summary = f'Accessability scanner found <span class="py-1 px-3 text-center font-semibold text-slate-100 rounded bg-red-600">{violations_total}</span> violation{"s" if violations_total > 1 else ""}'
    violations_summary_table = simplify_axe_result_for_summary(violations)
    violations_details = []
    for issue_index, issue in enumerate(violations):
        nodes_data = []
        for node_index, node in enumerate(issue["nodes"]):
            target_nodes = "\n".join(node["target"])
            html = node["html"]
            failure_summary = (
                "failureSummary" in node and node["failureSummary"] or None
            )
            any_nodes = node["any"]
            default_highlight = {
                "highlight": "Recommendation with the fix was not provided by axe result"
            }
            fix_summaries = (
                failure_summary
                and prepare_fix_summary(
                    failure_summary=failure_summary, default_highlight=default_highlight
                )
                or [default_highlight]
            )
            related_nodes_any = []
            for check_result in any_nodes:
                related_nodes = check_result["relatedNodes"]
                for related_node in related_nodes:
                    if related_node["target"]:
                        related_nodes_any.append("\n".join(related_node["target"]))
            nodes_data.append(
                {
                    "target_nodes": target_nodes,
                    "html": html,
                    "fix_summaries": fix_summaries,
                    "related_nodes_any": related_nodes_any,
                    "index": node_index + 1,
                }
            )
        issue["nodes"] = nodes_data
        issue["index"] = issue_index + 1
        issue["wcag"] = get_wcag_reference(issue["tags"])
        issue["impact"] = issue["impact"] or "n/a"
        violations_details.append(issue)
    return {
        "violations_summary": violations_summary,
        "violations_summary_table": violations_summary_table,
        "violation_details": violations_details,
        "checks_passed": passed_checks,
        "checks_incomplete": incomplete_checks,
        "checks_inapplicable": inapplicable_checks,
    }


def save_html_report(
    html_content,
    report_file_name="result.html",
    output_dir="artifacts",
    output_dir_path=os.getcwd(),
):
    """
    Saves the HTML report to a file.

    Args:
        html_content (str): The HTML content of the report.
        report_file_name (str, optional): The name of the report file. Defaults to "result.html".
        output_dir (str, optional): The name of the output directory. Defaults to "artifacts".
        output_dir_path (str, optional): The path to the output directory. Defaults to the current working directory.

    Raises:
        Exception: If an error occurs while trying to save the HTML report.

    Returns:
        None
    """
    try:
        report_directory = os.path.join(output_dir_path, output_dir)
        os.makedirs(report_directory, exist_ok=True)
        report_file_path = os.path.join(report_directory, report_file_name)
        try:
            os.remove(report_file_path)
        except FileNotFoundError:
            pass
        with open(report_file_path, "w", encoding="utf8") as file:
            file.write(html_content)
        logger.info(
            f"HTML report was saved into the following directory: {report_file_path}"
        )
    except Exception as e:
        logger.error(f"Error happened while trying to save html report: {e}")


def prepare_axe_rules(rules):
    """
    Prepare the Axe rules for processing.

    Args:
        rules (dict): A dictionary containing the Axe rules.

    Returns:
        list: A list of reformatted rules, each containing the index, rule ID, and enabled status.
    """
    reformatted_rules = []
    for index, rule_id in enumerate(rules.keys()):
        reformatted_rules.append(
            {"index": index + 1, "rule": rule_id, "enabled": rules[rule_id]["enabled"]}
        )
    return reformatted_rules


def get_html_report(results, options=None):
    """
    Generates an HTML accessibility report based on the given results.

    Args:
        results (dict): The accessibility results, including violations.
        options (dict, optional): Additional options for generating the report.

    Returns:
        dict or list: The generated HTML report data or an error message if the report generation fails.
    """
    if "violations" not in results:
        raise ValueError("'violations' is required for HTML accessibility report.")
    try:
        report_data = prepare_report_data(
            violations=results["violations"],
            passes=results.get("passes"),
            incomplete=results.get("incomplete"),
            inapplicable=results.get("inapplicable"),
        )
        report_data["project_url"] = results.get("url")
        report_data["violations"] = report_data.get("violations_summary_table")
        report_data["rules"] = prepare_axe_rules(rules=options.get("rules"))
        return report_data
    except Exception as e:
        logging.error(e, exc_info=True)
        return [f"Failed to create HTML report due to an error: {e}"]


def create_html_report(results, options=None):
    """
    Create an HTML accessibility report based on the given results.

    Args:
        results (dict): The accessibility results, including violations.
        options (dict, optional): Additional options for report generation.

    Returns:
        str: The HTML content of the generated report.

    Raises:
        ValueError: If 'violations' key is not present in the results.

    """
    if "violations" not in results:
        raise ValueError("'violations' is required for HTML accessibility report.")
    try:
        template_path = "django_axe/report.html"
        report_data = prepare_report_data(
            violations=results["violations"],
            passes=results.get("passes"),
            incomplete=results.get("incomplete"),
            inapplicable=results.get("inapplicable"),
        )
        report_data["project_url"] = results.get("url")
        report_data["violations"] = report_data.get("violations_summary_table")
        report_data["rules"] = prepare_axe_rules(rules=options.get("rules"))
        html_content = render_to_string(
            template_name=template_path, context=report_data
        )
        save_html_report(
            html_content=html_content,
            report_file_name=options.get("report_file_name"),
            output_dir=options.get("output_dir"),
            output_dir_path=options.get("output_dir_path"),
        )
        return html_content
    except Exception as e:
        logging.error(e, exc_info=True)
        return f"Failed to create HTML report due to an error: {e}"


def generate_html_from_json(report_path, options=None):
    """
    Generates an HTML report from a JSON file.

    Args:
        report_path (str): The path to the JSON file.
        options (dict, optional): Additional options for report generation. Defaults to None.

    Returns:
        str: A message indicating the result of the report generation.
    """
    if os.path.exists(report_path):
        with open(report_path, "r") as json_file:
            data = json.load(json_file)
            create_html_report(results=data, options=options)
            logger.info(
                f"HTML report was generated from the following path: {report_path}"
            )
            return f"HTML report was generated from the following path: {report_path}"
    else:
        logger.info(f"Report file was not found at the following path: {report_path}")
    return f"Report file was not found at the following path: {report_path}"


def create_sample_json_result_file(file_path):
    """
    Creates a sample JSON result file.

    Args:
        file_path (str): The path to the JSON result file.

    Returns:
        None
    """
    write_json(file_path=file_path, data=SAMPLE_REPORT)


def upsert_json_result_file(file_path, new_data, url):
    """
    Upserts the JSON result file with new data.

    If the file does not exist, it creates a new file with the new data.
    If the file exists, it merges the new data with the existing data and updates the file.

    Args:
        file_path (str): The path to the JSON result file.
        new_data (dict): The new data to be merged with the existing data.
        url (str): The URL associated with the new data.

    Returns:
        None
    """

    if not os.path.exists(file_path):
        create_sample_json_result_file(file_path)

    old_data = read_json_result_file(file_path)

    old_data = insert_new_data(
        old_data=old_data, new_data=new_data, key="violations", path=url
    )
    old_data = insert_new_data(old_data=old_data, new_data=new_data, key="inapplicable")
    old_data = insert_new_data(old_data=old_data, new_data=new_data, key="incomplete")
    old_data["toolOptions"] = new_data["toolOptions"]
    old_data["timestamp"] = new_data["timestamp"]
    old_data["testEngine"] = new_data["testEngine"]
    write_json(file_path=file_path, data=old_data)


def delete_json_result_file(file_path):
    """
    Deletes the JSON result file.

    Args:
        file_path (str): The path to the JSON result file.

    Returns:
        None
    """
    try:
        os.remove(file_path)
    except Exception as e:
        logger.error(e)


def read_json_result_file(file_path):
    """
    Reads a JSON result file and returns its contents as a Python object.

    Args:
        file_path (str): The path to the JSON result file.

    Returns:
        dict: The contents of the JSON file as a Python dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.

    """
    with open(file_path, "r") as file:
        return json.load(file)


def write_json(file_path, data):
    """
    Write data to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (dict): The data to be written to the file.

    Returns:
        None
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def insert_new_data(old_data, new_data, key, path=False):
    """
    Inserts new data into the old data based on a specified key.

    Args:
        old_data (dict): The existing data to be updated.
        new_data (dict): The new data to be inserted.
        key (str): The key in the new data to use for insertion.
        path (bool, optional): Indicates whether to include a path in the new items. Defaults to False.

    Returns:
        dict: The updated old data with the new items inserted.

    """
    if key in new_data:
        for new_item in new_data[key]:
            if path:
                new_item["path"] = path
            if not is_duplicate(new_item=new_item, old_data=old_data, key=key):
                old_data[key].append(new_item)
    return old_data


def is_duplicate(new_item, old_data, key):
    """
    Check if a new item is a duplicate based on a specific key in the old data.

    Args:
        new_item (dict): The new item to check for duplication.
        old_data (dict): The old data containing the items to compare against.
        key (str): The key to use for comparison.

    Returns:
        bool: True if the new item is a duplicate, False otherwise.
    """
    new_value_str = json.dumps(new_item, sort_keys=True)
    return any(
        [
            new_value_str == json.dumps(old_item, sort_keys=True)
            for old_item in old_data[key]
        ]
    )


def ignore_django_axe(view_func):
    """
    Decorator function to ignore Django Axe accessibility checks for a specific view function.

    Args:
        view_func (function): The view function to be decorated.

    Returns:
        function: The decorated view function.

    """

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        request.META["axe_ignore"] = True
        return view_func(request, *args, **kwargs)

    return wrapper
