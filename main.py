import streamlit as st
import mysql.connector
import pandas as pd
st.title(":violet[CUSTOMER MANAGEMENT SYSTEM]")
st.write("---")
choice=st.sidebar.selectbox("MyMenu",("\U0001F3E0 Home","\U0001F9D1 Register an Account","\U0001F4CC Login"))
if(choice=="\U0001F3E0 Home"):
    st.header(":blue[WELCOME]"":sunglasses:")
    st.write("* Hello This is an Application developed by **Shubham kumar** as a part of Training Project")
    st.image("https://previews.123rf.com/images/redeer/redeer1604/redeer160400003/54575173-customer-relationship-management-vector-illustration-flat-icons-of-clients-objectives-support.jpg")
    st.subheader("What is Customer Management System ?")
    st.success("* A customer management system is a cluster of all the **systems, processes, and applications** that are needed to manage customer relationships. It is also commonly known as **Customer Relationship Management**.")
    st.success("* A **Customer Management System** simplifies this by giving sales representatives a detailed view of **client records** so they can send personalized responses and reply within context.")
    st.markdown("* **Here you can:** [Learn More >](https://www.leadsquared.com/learn/sales/what-is-customer-management-system/)about this project.")
elif(choice=="\U0001F9D1 Register an Account"):
        usd=st.text_input("Enter user Id")
        usrname=st.text_input("Enter user_name")
        mobileno=st.text_input("Enter user_mobileno")
        psd=st.text_input("Enter user password",type='password')
        btn=st.button("Create my account")
        if btn:
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customermanagementsystem")
            c=mydb.cursor()
            c.execute("insert into Register values(%s,%s,%s,%s)",(usd,usrname,mobileno,psd))
            mydb.commit()
            st.success("Account created Successfully as {}".format(usrname))
            st.info("Go to Login Menu to Login")
elif choice=="\U0001F4CC Login":
        if 'login' not in st.session_state:
            st.session_state['login']=False
        usd=st.text_input("Enter user Id")
        psd=st.text_input("Enter user password",type='password')
        btn=st.button("Login")
        if btn:
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customermanagementsystem")
            c=mydb.cursor()
            mydb.commit()
            c.execute("select * from Register")
            for r in c:
                if(r[0]==usd and r[3]==psd):
                    st.session_state['login']=True
                    break
            if(st.session_state['login']==False):
                st.warning("Incorrect ID or Password")
        if(st.session_state['login']==True):
            st.success("Login Successfull")
            st.balloons()
            choice2=st.selectbox("Features",("None","Add Customer","Search Customer","View All Customer","Registered Customers"))
            if(choice2=="Add Customer"):
                cid=st.text_input("Enter customer Id")
                csrname=st.text_input("Enter customer name")
                cusmail=st.text_input("Enter customer email")
                age=st.text_input("Enter your age")
                gnd=st.text_input("Enter your gender")
                address=st.text_input("Enter your  address")
                no=st.text_input("Enter your phone number")
                st.checkbox("I Agree")
                btn2=st.button("Add")
                if(btn2):
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customermanagementsystem")
                    c=mydb.cursor()
                    c.execute("insert into customers values(%s,%s,%s,%s,%s,%s,%s)",(cid,csrname,cusmail,age,gnd,address,no))
                    mydb.commit()
                    st.success("Customer details added successfully")
            elif(choice2=="Search Customer"):
                if 'alogin' not in st.session_state:
                    st.session_state['alogin']=False
                cid=st.text_input("Enter customer Id")
                csrname=st.text_input("Enter customer name")
                btn=st.button("Search")
                if btn:
                    mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customermanagementsystem")
                    c=mydb.cursor()
                    mydb.commit()
                    c.execute("select * from customers")
                    for r in c:
                        if(r[0]==cid and r[1]==csrname):
                            st.session_state['alogin']=True
                            break
                    if(st.session_state['alogin']==False):
                        st.warning("Incorrect ID or Name")
                if(st.session_state['alogin']==True):
                    st.success("Correct Details")
            elif(choice2=="View All Customer"):
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customermanagementsystem")
                c=mydb.cursor()
                c.execute("select * from customers")
                l=[]
                for r in c:
                    l.append(r)
                df=pd.DataFrame(data=l,columns=['cus_id','cus_Name','cus_email','cus_age','cus_gender','cus_address','cus_phoneNo']) 
                st.dataframe(df)
                
            elif(choice2=="Registered Customers"):
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customermanagementsystem")
                c=mydb.cursor()
                c.execute("select * from Register")
                l=[]
                for r in c:
                    l.append(r)
                df=pd.DataFrame(data=l,columns=['user_id','user_name','user_mobileno','user_password']) 
                st.dataframe(df)



