from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class NLPapp:

    def __init__(self):
        self.myapi = API()
        self.dbo = Database()
        self.root = Tk()
        self.root.title("NLPApp")
        self.root.geometry('350x600')
        self.root.configure(bg = "#34495E")
        self.login_gui()



        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text="NLPApp")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        lable1 = Label(self.root,text="Enter Email")
        lable1.pack(pady=(10,5))
        lable1.configure(font=('verdana',10,'bold'))

        self.Email_input = Entry(self.root,width=50)
        self.Email_input.pack(pady=(10,10))

        lable2= Label(self.root, text="Enter Password")
        lable2.pack(pady=(10, 5))
        lable2.configure(font=('verdana', 10, 'bold'))

        self.Password_input = Entry(self.root, width=50,show = '*')
        self.Password_input.pack(pady=(10, 10))

        login_btn = Button(self.root, text="Log IN",height=2,width=30,command=self.perform_login)
        login_btn.pack(pady=(10, 5))
        login_btn.configure(font=('verdana', 10, 'bold'),bg="#3333ff")

        redirect_btn = Button(self.root, text="Not a Member register Here",command=self.register_gui)
        redirect_btn.pack(pady=(10, 5))
        redirect_btn.configure(font=('verdana', 10, 'bold'),bg="#3333ff")

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        lable0 = Label(self.root, text="Enter Name")
        lable0.pack(pady=(10, 5))
        lable0.configure(font=('verdana', 10, 'bold'))

        self.Name_input = Entry(self.root, width=50)
        self.Name_input.pack(pady=(10, 10))

        lable1 = Label(self.root, text="Enter Email")
        lable1.pack(pady=(10, 5))
        lable1.configure(font=('verdana', 10, 'bold'))

        self.Email_input = Entry(self.root, width=50)
        self.Email_input.pack(pady=(10, 10))

        lable2 = Label(self.root, text="Enter Password")
        lable2.pack(pady=(10, 5))
        lable2.configure(font=('verdana', 10, 'bold'))

        self.Password_input = Entry(self.root, width=50)
        self.Password_input.pack(pady=(10, 10))

        registration_btn = Button(self.root, text="Register", height=2, width=30,command=self.perform_registration)
        registration_btn.pack(pady=(10, 5))
        registration_btn.configure(font=('verdana', 10, 'bold'), bg="#3333ff")

        lable3 = Label(self.root, text="already a member")
        lable3.pack(pady=(10, 5))
        lable3.configure(font=('verdana', 10, 'bold'))

        redirect_btn = Button(self.root, text="Login now",command=self.login_gui)
        redirect_btn.pack(pady=(10, 5))
        redirect_btn.configure(font=('verdana', 10, 'bold'), bg="#3333ff")


    def clear(self):
        # clear the existing gui
        for  i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name = self.Name_input.get()
        Email = self.Email_input.get()
        Password = self.Password_input.get()

        response = self.dbo.add_data(name,Email,Password)

        if response:
            messagebox.showinfo('Succes',"Registration Successful. You can login now")

        else:
            messagebox.showerror('Error','Email already exists')

    def perform_login(self):
        Email = self.Email_input.get()
        Password = self.Password_input.get()

        response = self.dbo.search_data(Email,Password)

        if response:
            messagebox.showinfo('success','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email/password')
    def home_gui(self):
        self.clear()
        heading = Label(self.root,text = "NLPApp",bg ='#34495E',fg='white' )
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_btn = Button(self.root,text='Sentiment Analysis',width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))
        sentiment_btn.configure(font=('verdana',24,'bold'))

        ner_btn = Button(self.root, text='NER', width=30, height=4)
        ner_btn.pack(pady=(10, 10))
        ner_btn.configure(font=('verdana',24,'bold'))

        emotion_btn = Button(self.root, text='Emotion Analysis', width=30, height=4)
        emotion_btn.pack(pady=(10, 10))
        emotion_btn.configure(font=('verdana',24,'bold'))

        home_btn = Button(self.root,text='Home Page',width= 10,command=self.login_gui)
        home_btn.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        lable1 = Label(self.root, text="Enter Text")
        lable1.pack(pady=(10, 5))
        lable1.configure(font=('verdana', 10, 'bold'))

        self.Sentiment_input = Entry(self.root, width=50)
        self.Sentiment_input.pack(pady=(10, 10))

        sentiment_btn = Button(self.root,text="Sentiment Analysis",width=40,command=self.do_sentiment)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',24))


        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment(self) :
        text = self.Sentiment_input.get()
        result = self.myapi.sentiment_analysis(text)

        txt = ""
        for i in result['sentiment'] :
            sentiment_value = result['sentiment'][i]

            # Check if the sentiment_value is a list or a single float
            if isinstance(sentiment_value, list) :
                sentiment_value = ', '.join(str(val) for val in sentiment_value)
            else :
                sentiment_value = str(sentiment_value)

            txt += i + ' -> ' + sentiment_value + '\n'

        print(txt)
        self.sentiment_result.config(text=txt)  # Update the Label widget with the result


nlp = NLPapp()
