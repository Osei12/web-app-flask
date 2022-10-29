from flask import Flask, render_template,request,redirect,url_for,flash,get_flashed_messages,Response
from extensions import db,migrate
import uuid as uuid
from werkzeug.utils import secure_filename
import os
import io
import xlwt

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:iPo4igoQLhF4hOsKj2vW@containers-us-west-107.railway.app:7508/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'dghdgjhggghGHJGHFTRETY%$$%$^76786'

UPLOAD_FOLDER = 'static/images/profile/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)
migrate.init_app(app,db)

##### ROUTES

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/add_new_member',methods=['GET','POST'])
def add():
    members = MemberRecords.query.all()
    if request.method=='GET':
         return render_template('add.html', members=members)
    if request.method=='POST':
        dp = request.form.getlist('department')
        department=",".join(map(str,dp))
        
        surname = request.form['surname']
        other_names = request.form['other_names']
        gender = request.form['gender']
        dob = request.form['dob']
        occupation = request.form['occupation']
        inst_of_work = request.form['inst_of_work']
        fathers_name= request.form['fathers_name']
        motality_father= request.form['motality_father']
        mothers_name= request.form['mothers_name']
        motality_mother= request.form['motality_mother']
        marital_status= request.form['marital_status']
        email= request.form['email']
        phone= request.form['mobile_number']
        emergency_contact_name= request.form['emergency_contact_person']
        relations= request.form['relations']
        emergency_contact_no= request.form['emergency_contact_no']
        no_of_children= request.form['no_of_children']
        place_of_residence= request.form['place_of_residence']
        house_no= request.form['house_no']
        gps_address= request.form['gps_address']
        prominent_landmark= request.form['prominent_landmark']
        hometown= request.form['hometown']
        region= request.form['region']
        level_of_education= request.form['level_of_education']
        name_of_basic_sch= request.form['name_basic_sch']
        name_of_2nd_cycle_sch= request.form['name_of_2nd_cycle_sch']
        name_of_tertiary_sch= request.form['name_tertiary_sch']
        courses_offered= request.form['courses_offered']
        post_grad_courses_offered= request.form['post_grad_courses']
        when_were_you_born_again= request.form['when_were_born_again']
        when_did_you_join_the_church= request.form['when_did_you_join_the_church']
        baptized_by_immersion= request.form['baptized_by_immersion']
        baptized_by_holy_spirit= request.form['baptized_by_holy_spirit']
        active_in_department= request.form['active_department']

        department=department
        profile = request.files['upload']
      
        pic_filename = secure_filename(profile.filename)
        pic_name = str(uuid.uuid1()) + " _ " + pic_filename
        saver = request.files['upload']
        saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        profile=pic_name
    
        members = MemberRecords(
            
            surname=surname,
            other_names=other_names,
            gender=gender,
            dob=dob,
            occupation=occupation,
            inst_of_work=inst_of_work,
            fathers_name=fathers_name,
            mortality_father=motality_father,
            mothers_name=mothers_name,
            mortality_mother=motality_mother,
            marital_status=marital_status,
            email=email,
            phone=phone,
            emergency_contact_name=emergency_contact_name,
            relations=relations,
            emergency_contact_no=emergency_contact_no,
            no_of_children=no_of_children,
            place_of_residence=place_of_residence,
            house_no=house_no,
            gps_address=gps_address,
            prominent_landmark=prominent_landmark,
            hometown=hometown,
            region=region,
            level_of_education=level_of_education,
            name_of_basic_sch=name_of_basic_sch,
            name_of_2nd_cycle_sch=name_of_2nd_cycle_sch,
            name_of_tertiary_sch=name_of_tertiary_sch,
            courses_offered=courses_offered,
            post_grad_courses_offered=post_grad_courses_offered,
            when_were_you_born_again=when_were_you_born_again,
            when_did_you_join_the_church=when_did_you_join_the_church,
            baptized_by_immersion=baptized_by_immersion,
            baptized_by_holy_spirit=baptized_by_holy_spirit,
            active_in_department=active_in_department,
            profile=profile,
            department=department
            
        )
        db.session.add(members)
        db.session.commit()
        flash('Member added succesfuly')
        return redirect(url_for('add'))
    return render_template('add.html')


@app.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    
    member = MemberRecords.query.get_or_404(id)
    if request.method=="POST":
      
        if member:
            dp = request.form.getlist('department')
            department=",".join(map(str,dp))
           
            member.surname = request.form['surname']
            member.other_names = request.form['other_names']
            member.gender = request.form['gender']
            member.dob = request.form['dob']
            member.occupation = request.form['occupation']
            member.fathers_name= request.form['fathers_name']
            member.motality_father= request.form['motality_father']
            member.mothers_name= request.form['mothers_name']
            member.motality_mother= request.form['motality_mother']
            member.marital_status= request.form['marital_status']
            member.email= request.form['email']
            member.phone= request.form['mobile_number']
            member.emergency_contact_name= request.form['emergency_contact_person']
            member.relations= request.form['relations']
            member.emergency_contact_no= request.form['emergency_contact_no']
            member.no_of_children= request.form['no_of_children']
            member.place_of_residence= request.form['place_of_residence']
            member.house_no= request.form['house_no']
            member.gps_address= request.form['gps_address']
            member.prominent_landmark= request.form['prominent_landmark']
            member.hometown= request.form['hometown']
            member.region= request.form['region']
            member.level_of_education= request.form['level_of_education']
            member.name_of_basic_sch= request.form['name_basic_sch']
            member.name_of_2nd_cycle_sch= request.form['name_of_2nd_cycle_sch']
            member.name_of_tertiary_sch= request.form['name_tertiary_sch']
            member.courses_offered= request.form['courses_offered']
            member.post_grad_courses_offered= request.form['post_grad_courses']
            member.when_were_you_born_again= request.form['when_were_born_again']
            member.when_did_you_join_the_church= request.form['when_did_you_join_the_church']
            member.baptized_by_immersion= request.form['baptized_by_immersion']
            member.baptized_by_holy_spirit= request.form['baptized_by_holy_spirit']
            member.active_in_department= request.form['active_department']
            member.department=department
    
            if request.files['upload']:
                member.profile = request.files['upload']
                member.profile=request.files['upload']
                pic_filename = secure_filename( member.profile.filename)
                pic_name = str(uuid.uuid1()) + " _ " + pic_filename
                saver = request.files['upload']
                saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
                member.profile=pic_name                
                db.session.commit()
                flash('Updated succesfuly')
                return redirect(url_for('member_list'))
            else:
                 
                db.session.commit()
                flash('Updated succesfuly')
                return redirect(url_for('member_list'))
                
    return render_template('update.html', member = member)

@app.route('/member_list', methods=['GET', 'POST'])
def member_list():
    members = MemberRecords.query.all()
    return render_template('list.html', members=members)

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    member = MemberRecords.query.get_or_404(id)
    if member:
        db.session.delete(member)
        db.session.commit()
        member = MemberRecords.query.all()
        flash('Deleted succesfuly')
        return redirect(url_for('member_list'))
    
    return render_template('list.html', member=member)




# @app.route('/downlaod/report/excel')
# def download_report():
#     all_members = MemberRecords.query.all()
#     output = io.BytesIO()
    
#     workbook = xlwt.Workbook()
    
#     sh = workbook.add_sheet('Member Report')
#     sh.write(0, 0, 'Id')
#     sh.write(0, 1, 'Surname')
#     sh.write(0, 2, 'Other Names')
#     sh.write(0, 3, 'Gender')
#     sh.write(0, 4, 'Date of Birth')
#     sh.write(0, 5, 'Occupation')
#     sh.write(0, 6, "Inst of work")
#     sh.write(0, 7, "Father's name")
#     sh.write(0, 8, 'Dead or Alive')
#     sh.write(0, 9, "Mother's name")
#     sh.write(0, 10, 'Dead orAlive')
#     sh.write(0, 11, 'Marital Status')
#     sh.write(0, 12, 'Email')
#     sh.write(0, 13, 'Phone')
#     sh.write(0, 14, 'Emergency contact person')
#     sh.write(0, 15, 'Relations')
#     sh.write(0, 16, 'Emergency contact no')
#     sh.write(0, 17, 'No of children')
#     sh.write(0, 18, 'Place of residence')
#     sh.write(0, 19, 'House no')
#     sh.write(0, 20, 'Gps address')
#     sh.write(0, 21, 'Prominent Landmark')
#     sh.write(0, 22, 'Hometown')
#     sh.write(0, 23, 'Region')
#     sh.write(0, 24, 'Level of education')
#     sh.write(0, 25, 'Name of Basic sch')
#     sh.write(0, 26, 'Name of 2nd cycle sch')
#     sh.write(0, 27, 'Name of tertiary sch')
#     sh.write(0, 28, 'Courses offered')
#     sh.write(0, 29, 'Post graduate courses offered')
#     sh.write(0, 30, 'When were you born again')
#     sh.write(0, 31, 'When did you join the church')
#     sh.write(0, 32, 'Baptized by immersion')
#     sh.write(0, 33, 'Baptized by Holy Spirit')
#     sh.write(0, 34, 'Active in any department')
#     sh.write(0, 35, 'Department')

    
#     idx=0
#     for member in all_members:
#         sh.write(idx+1, 0, str(member.id))
#         sh.write(idx+1, 1,  member.surname)
#         sh.write(idx+1, 2, member.other_names)
#         sh.write(idx+1, 3, member.gender)
#         sh.write(idx+1, 4, member.dob)
#         sh.write(idx+1, 5, member.occupation)
#         sh.write(idx+1, 6, member.inst_of_work)
#         sh.write(idx+1, 7, member.fathers_name)
#         sh.write(idx+1, 8, member.mortality_father)
#         sh.write(idx+1, 9, member.mothers_name)
#         sh.write(idx+1, 10, member.mortality_mother)
#         sh.write(idx+1, 11, member.marital_status)
#         sh.write(idx+1, 12, member.email)
#         sh.write(idx+1, 13, member.phone)
#         sh.write(idx+1, 14, member.emergency_contact_name)
#         sh.write(idx+1, 15, member.relations)
#         sh.write(idx+1, 16, member.emergency_contact_no)
#         sh.write(idx+1, 17, member.no_of_children)
#         sh.write(idx+1, 18, member.place_of_residence)
#         sh.write(idx+1, 19, member.house_no)
#         sh.write(idx+1, 20, member.gps_address)
#         sh.write(idx+1, 21, member.prominent_landmark)
#         sh.write(idx+1, 22, member.hometown)
#         sh.write(idx+1, 23, member.region)
#         sh.write(idx+1, 24, member.level_of_education)
#         sh.write(idx+1, 25, member.name_of_basic_sch)
#         sh.write(idx+1, 26, member.name_of_2nd_cycle_sch)
#         sh.write(idx+1, 27, member.name_of_tertiary_sch)
#         sh.write(idx+1, 28, member.courses_offered)
#         sh.write(idx+1, 29, member.post_grad_courses_offered)
#         sh.write(idx+1, 30, member.when_were_you_born_again)
#         sh.write(idx+1, 31, member.when_did_you_join_the_church)
#         sh.write(idx+1, 32, member.baptized_by_immersion)
#         sh.write(idx+1, 33, member.baptized_by_holy_spirit)
#         sh.write(idx+1, 34, member.active_in_department)
#         sh.write(idx+1, 35, member.department)
    
#         idx+= 1
        
#     workbook.save(output)
#     output.seek(0)
#     return Response(output, mimetype="application/ms-excel",headers={"Content-Disposition":"attachment;filename=member_reports.xls"} )


from models import MemberRecords

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run()