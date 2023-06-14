from flask import Flask, render_template, redirect, request, flash, url_for
from models import Department, Employees, Project, Location
from config import SECRET_KEY

from database import db_session, init_db
from sqlalchemy import select


app = Flask(__name__)
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY



with app.app_context():
    init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.close()


@app.route('/')
def show_all():
    departments = Department.query.all()
    return render_template('show_all.html', departments=departments)


@app.route('/department', methods=['GET', 'POST'])
def newdepartment():
    if request.method == 'POST':
        if not request.form['dname'] or not request.form['dnumber']:
            flash('Please enter all the fields', 'error')
        else:
            name=db_session.query(Department).filter(Department.dname==request.form['dname']).first()
            number=db_session.query(Department).filter(Department.dnumber==request.form['dnumber']).first()
            if (name != None) or (number != None):
                flash('The name and the number must be unique', 'error')
            else:
                department = Department(
                    dname=request.form['dname'], dnumber=request.form['dnumber'])
                db_session.add(department)
                db_session.commit()
                flash('Record was successfully added')
                return redirect(url_for('show_all'))
    return render_template('new_department.html')


@app.route('/list-of-employees/<dnumber>', methods=['GET'])
def list_employees(dnumber):
    department = Department.query.get(dnumber)
    return render_template('employees.html', emps=department.emps, department=department)

@app.route('/list-of-employees/delete/<int:ssn>', methods=['POST'])
def del_employee(ssn): 
    employee=db_session.query(Employees).filter(Employees.ssn==ssn).first()
    dnumber=employee.dno
    db_session.delete(employee)
    db_session.commit()
    message = f"Employee {employee.fname} {employee.lname} with SSN:{employee.ssn} has been deleted"
    flash(message)
    return redirect(url_for('list_employees',dnumber=dnumber))
 

@app.route('/employee/<dnumber>', methods=['GET'])
def create_employee(dnumber):
    department = db_session.get(Department, dnumber)
    return render_template('new_employee.html', department=department)


@app.route('/employee/<dnumber>', methods=['POST'])
def save_employee(dnumber):
    if not request.form['fname'] or not request.form['lname'] or not request.form['ssn']:
        flash('Please enter all the fields', 'error')
    else:
        ssn=db_session.query(Employees).filter(Employees.ssn==request.form['ssn']).first()
        if ssn != None:
            flash('The ssn must be unique', 'error')
        else: 
            deps=Department.query.get(dnumber)
            employee = Employees(fname=request.form['fname'], lname=request.form['lname'],ssn=request.form['ssn'],salary=request.form['salary'], deps=deps)
            db_session.add(employee)
            db_session.commit()
            flash('Record was successfully added')
            return redirect(url_for('list_employees',dnumber=dnumber))
    
    return render_template('new_employee.html', department=Department.query.get(dnumber))
    


@app.route('/list-of-projects/<dnumber>', methods=['GET'])
def list_projects(dnumber):
    department = Department.query.get(dnumber)
    return render_template('projects.html', pro=department.pro, department=department)


@app.route('/project/<dnumber>', methods=['GET'])
def create_project(dnumber):
    department = db_session.get(Department, dnumber)
    return render_template('new_project.html', department=department, Location=Location)


@app.route('/project/<dnumber>', methods=['POST'])
def save_project(dnumber):
    if not request.form['pname'] or not request.form['plocation'] or not request.form['pnumber']:
        flash('Please enter all the fields', 'error')
    else:
        pnumber=db_session.query(Project).filter(Project.pnumber==request.form['pnumber']).first()
        pname=db_session.query(Project).filter(Project.pname==request.form['pname']).first()
        if pnumber != None or pname != None:
            flash("The project's name and number must be unique", "error")
        else: 
            depart=Department.query.get(dnumber)
            project = Project(pname=request.form['pname'], plocation=request.form['plocation'],pnumber=request.form['pnumber'], depart=depart)
            db_session.add(project)
            db_session.commit()
            flash('Record was successfully added')
    return redirect(url_for('show_all'))


@app.route('/list-of-projects/delete/<int:pnumber>', methods=['POST'])
def del_project(pnumber): 
    project=db_session.query(Project).filter(Project.pnumber==pnumber).first()
    dnumber=project.dnum
    db_session.delete(project)
    db_session.commit()
    return redirect(url_for('list_projects',dnumber=dnumber))

