from flask import Flask, request, render_template_string

app = Flask(__name__)

# Route to handle form submission and display the results
@app.route('/', methods=['GET', 'POST'])
def poll_form():
    if request.method == 'POST':
        # Extract data from the form
        name = request.form.get('name')
        zcode = [request.form.get('zcode')]
        issue = request.form.get('issue')

        # Print the extracted data
        print(f"Name: {name}")
        print(f"Zip Code: {zcode}")
        print(f"Issue: {issue}")

        # You can return the data or redirect to a new page
        return f"Form submitted! Name: {name}, Zip Code: {zcode}, Issue: {issue}"

    return render_template_string("""
        <form id="pollForm" method="POST">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br><br>

            <label for="zcode">Zip Code:</label><br>
            <input type="text" id="code" name="zcode" placeholder="Enter the zip code of the issue here" required><br><br>

            <br>
            <label for="offense">Choose the Issue Occurred:</label><br>
            <input type="radio" id="assault" name="issue" value="Assault">
            <label for="assault">Assault</label><br>
            <input type="radio" id="misconduct" name="issue" value="Police Misconduct">
            <label for="misconduct">Police Misconduct</label><br>
            <input type="radio" id="discrimination" name="issue" value="Discrimination">
            <label for="discrimination">Discrimination</label><br>
            <input type="radio" id="environmental" name="issue" value="Environmental Hazard">
            <label for="environmental">Environmental Hazard</label><br><br>

            <input type="submit" value="Submit"><br><br>
        </form>
    """)

if __name__ == '__main__':
    app.run(debug=True)
