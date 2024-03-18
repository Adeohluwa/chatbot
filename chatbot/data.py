from .db import get_answered_enquiries

faq_data = {
      "What type of halls are available to students in the main campus?": "We have Premium halls and classic halls for both male and female.",
      "How is hostel accommodation assigned to students?": "We offer both premium and classic halls, each designated for specific academic levels. Depending on your level and selected plan, students have the flexibility to choose the hall that best aligns with their preferences.",
      "What are the costs of different types of hostel accommodation?": "This information is available on our website.",
      "How is the allocation of rooms to students determined?": "The allocation of rooms to students is done on a first-come, first-served basis.",
      "What are the premium halls available to male students?": "Check the school’s UMIS page for the information.",
      "What are the classic halls available to male students?": "Check the school’s UMIS page for the information.",
      "What are the premium halls available to female students?": "Check the school’s UMIS page for the information.",
      "What are the classic halls available to female students?": "Check the school’s UMIS page for the information.",
      "Can parents visit the hostel facilities before the academic year begins?": "Yes, parents are welcome to visit the hostel facilities.",
      "Are there any specific requirements or documentation needed for hostel registration?": "Yes, the student needs to come with a student receipt or course form, ID card, and passport photograph, then further instructions would be given to the students on how to register when they are at the school premises.",
      "What amenities are provided in the hostel rooms?": "Hostel rooms are equipped with chairs, tables, fans, wardrobes, bunk beds, and toilets.",
      "Is there a separate hostel for male and female students?": "Yes, we have separate hostels for male and female students.",
      "What security measures are in place within the hostel premises?": "The hostel premises are equipped with security personnel, surveillance cameras to ensure the safety and security of all residents.",
      "Are laundry services been rendered to students in the hostel?": "Yes, they are, but the students are to pay for the services.",
      "How are maintenance issues and repairs addressed in the hostel?": "Students can report maintenance issues to the porters, and our maintenance team promptly addresses and resolves any concern.",
      "Are there curfew hours for hostel residents?": "Yes, the students are expected to return to their various halls on or before 21:45.",
      "What is the process for handling medical emergencies in the hostel?": "In the event of a medical emergency in the hostel, the student is rushed to the hospital by the ambulance, where the student will be taken care of.",
      "Are cooking facilities available for students within the hostel?": "No, the students are not allowed to cook within the hostel premises.",
      "Is it permissible for students to reside off-campus?": "Yes, students can reside off-campus if they choose to do so.",
      "What measures are in place to ensure the safety of belongings in the hostel?": "Regarding the safety of belongings, students with laptops are required to register them at the reception before bringing them into the halls. Additionally, CCTV cameras have been installed in the halls to monitor the student activities.",
      "What is the policy on hostel fees?": "Students can pay their hostel fees online through the university’s student portal (UMIS). Hostel fees are based on the type of hostel accommodation.",
      "Are there any additional costs associated with hostel accommodation?": "No, there are no additional costs associated with hostel accommodation; they are all included in the hostel fees.",
      "What transportation options are available for students living in the hostel?": "Our university provides tricycles as a transportation option for students living in the hostel.",
      "Are counselling services available for hostel residents?": "Yes, counselling services are available to hostel residents, professional counselling support is provided to assist students living in the hostel.",
      "Is there a system for reporting and addressing incidents of harassment within the hostel?": "Yes, Babcock university has a comprehensive system in place for reporting and addressing incidents of harassment within the hostel. We take any allegations of harassment seriously and encourage students to report such incidents promptly to the hall porters, SOP, or hall administrators.",
      "How are roommates' conflicts resolved in the hostel?": "Roommates' conflicts can be resolved by encouraging them to openly communicate their concerns amongst the other. The hostel staff may organize formal conflict resolution meetings where both roommates can discuss their concerns, and staff members can provide guidance on finding common ground. In cases where conflicts persist and resolution seems challenging, the option of room changes may be considered.",
      "How does the university handle cases of lost or misplaced belongings in the hostel?": "Our university advises students to promptly report any lost belongings to hostel staff. Hostel staff will initiate a search, checking each student's bags for the lost item until the items are found, then the hostel staff will notify the resident.",
      "How can parents stay updated on hostel events and important announcements?": "The university may provide an online portal, where parents can access information about hostel events, announcements. Also, regular email updates and newsletters may be sent to parents, highlighting upcoming hostel events, important announcements.",
      "Is there a provision for students to change rooms within the hostel if needed?": "Yes, there is a provision for students to change rooms within the hostel if needed. Students interested in changing rooms are advised to contact the hostel staff to inquire about the procedures and availability of alternative accommodation.",
      "Do the rooms have air conditioning?": "Just the new halls built recently in 2023 have air conditioners.",
      "What security measures are in place for students leaving the hostel for vacations?": "Each student would follow due process which would be specified by the hostel staff, upon completion of the process, the student would be given a hall pass, after signing out properly from both the hall and at the school main gate.",
      "How does the university handle the transition for first-year students entering hostel life?": "Our university organizes hostel orientation programs which are organized to familiarize first-year students with the hostel facilities, rules, and regulations. Also, dedicated hostel staff members are available to guide the first-year students through the initial stages of hostel life. The university carefully assigns a hall to the first-year students. And student handbooks are provided to the first-year students.",
      "Are there any pet restrictions in the hostels?": "Yes, pets are not allowed into the hostel premises.",
      "Are there any smoking or alcohol restrictions in the hostels?": "Smoking and drinking of alcohols are prohibited in the school premises.",
      "Are the hostels accessible to students with disabilities?": "Yes, they are.",
      "Are the rooms shared?": "Yes, but there is an exception for medical students.",
      "How many students can stay in a room?": "In classic halls, only 4 students can stay in a room, while in the premium halls only 6 people can stay in a room.",
      "Are there study rooms in the halls?": "Yes, they are.",
      "Are there shared bathrooms?": "Yes, the rooms have shared bathrooms.",
      "Are there common areas for hostel residents to relax?": "Yes, the students can relax at the reception, this area most times has couches, chairs, tables, and TVs."
}


bursary_data = {
    "How can I pay my tuition fees?": "Tuition fees can be paid through various methods including bank transfers, online payment portals, or in-person at the bursary office. Detailed instructions for each payment method are available on our website.",
    "Are there any scholarships or financial aid opportunities available for students?": "Yes, we offer a range of scholarships and financial aid programs for eligible students. Information about available scholarships and how to apply for financial aid can be found on our website or obtained from the bursary office.",
    "What is the deadline for tuition fee payment?": "The deadline for tuition fee payment is typically communicated to students via official channels such as email or the university's website. It's important to adhere to the deadlines to avoid late fees or registration holds.",
    "Can I request a payment plan for my tuition fees?": "Yes, students facing financial difficulties may request a payment plan through the bursary office. The availability of payment plans and the specific procedures for requesting one can be discussed with a bursary representative.",
    "How can I obtain a copy of my tuition fee receipt?": "You can obtain a copy of your tuition fee receipt by visiting the bursary office in person or by requesting one through email. Please provide your student ID and any other relevant information when making your request.",
    "What should I do if I have concerns about my tuition fees or financial aid package?": "If you have concerns about your tuition fees or financial aid package, we encourage you to schedule an appointment with a bursary advisor. They can provide guidance and assistance tailored to your specific situation."
}


registry_data = {
    "How do I register for courses each semester?": "Course registration is typically done online through the university's student portal. Detailed instructions and registration deadlines are provided to students prior to each semester.",
    "What should I do if I encounter difficulties during the course registration process?": "If you encounter difficulties during the course registration process, please contact the registry office for assistance. Our staff are available to help troubleshoot any issues you may experience.",
    "Can I change my course schedule after registration?": "Yes, students may be able to make changes to their course schedule during the designated add/drop period. However, changes are subject to availability and approval from academic advisors.",
    "Are there any prerequisites or co-requisites for certain courses?": "Yes, some courses may have prerequisites or co-requisites that students must fulfill before enrolling. This information is typically outlined in the course catalog or on the university's website.",
    "How do I know which courses to register for each semester?": "Students are advised to consult with their academic advisors or program coordinators to determine which courses they should register for each semester. Advisors can provide guidance based on program requirements and individual academic goals."
}


courses_data = {
    "What types of courses are offered at the university?": "The university offers a wide range of courses across various disciplines including arts, sciences, business, engineering, and more. Detailed course listings are available in the university catalog.",
    "Are there any specialized programs or tracks available within certain courses of study?": "Yes, some courses of study offer specialized programs or tracks for students with specific interests or career goals. Information about these programs can be obtained from academic advisors or program coordinators.",
    "How do I access course materials and resources?": "Course materials and resources are typically provided through the university's learning management system (LMS) or distributed by instructors at the beginning of the semester. Students can access these materials online or through designated course platforms.",
    "What is the process for withdrawing from a course?": "The process for withdrawing from a course may vary depending on the university's policies and procedures. Students are advised to consult with their academic advisors or the registry office for guidance on withdrawing from a course.",
    "Are there any opportunities for independent study or research within certain courses?": "Yes, some courses may offer opportunities for independent study or research projects under the guidance of faculty mentors. Interested students should speak with their instructors or academic advisors to explore these opportunities further."
}


exam_schedule_data = {
  "University Exam Schedule - Spring Semester 2024": [
    {
      "Date": "Monday, May 6",
      "Time": "9:00 AM",
      "Courses": [
        {
          "Course Code": "MATH 101",
          "Course Title": "Introduction to Calculus",
          "Location": "Lecture Hall A"
        },
        {
          "Course Code": "CHEM 201",
          "Course Title": "Organic Chemistry II",
          "Location": "Chemistry Lab"
        }
      ]
    },
    {
      "Date": "Tuesday, May 7",
      "Time": "10:00 AM",
      "Courses": [
        {
          "Course Code": "ENG 202",
          "Course Title": "British Literature",
          "Location": "Lecture Hall B"
        },
        {
          "Course Code": "BIO 301",
          "Course Title": "Molecular Biology",
          "Location": "Biology Lab"
        }
      ]
    },
    {
      "Date": "Wednesday, May 8",
      "Time": "11:00 AM",
      "Courses": [
        {
          "Course Code": "PSYCH 301",
          "Course Title": "Abnormal Psychology",
          "Location": "Psychology Building"
        },
        {
          "Course Code": "HIST 102",
          "Course Title": "World History II",
          "Location": "History Department"
        }
      ]
    },
    {
      "Date": "Thursday, May 9",
      "Time": "9:30 AM",
      "Courses": [
        {
          "Course Code": "PHYS 202",
          "Course Title": "Electromagnetism",
          "Location": "Physics Lab"
        },
        {
          "Course Code": "ART 103",
          "Course Title": "Introduction to Art History",
          "Location": "Art Building"
        }
      ]
    },
    {
      "Date": "Friday, May 10",
      "Time": "10:30 AM",
      "Courses": [
        {
          "Course Code": "ECON 201",
          "Course Title": "Microeconomics",
          "Location": "Economics Department"
        },
        {
          "Course Code": "POLI 202",
          "Course Title": "International Relations",
          "Location": "Political Science Building"
        }
      ]
    },
    {
      "Date": "Monday, May 13",
      "Time": "11:00 AM",
      "Courses": [
        {
          "Course Code": "CS 301",
          "Course Title": "Data Structures & Algorithms",
          "Location": "Computer Science Lab"
        },
        {
          "Course Code": "SOC 202",
          "Course Title": "Sociology of Gender",
          "Location": "Sociology Department"
        }
      ]
    },
    {
      "Date": "Tuesday, May 14",
      "Time": "9:00 AM",
      "Courses": [
        {
          "Course Code": "ENVS 201",
          "Course Title": "Environmental Science",
          "Location": "Environmental Lab"
        },
        {
          "Course Code": "MUSIC 101",
          "Course Title": "Music Appreciation",
          "Location": "Music Hall"
        }
      ]
    },
    {
      "Date": "Wednesday, May 15",
      "Time": "10:00 AM",
      "Courses": [
        {
          "Course Code": "COMM 301",
          "Course Title": "Public Speaking",
          "Location": "Communication Building"
        },
        {
          "Course Code": "GEOG 202",
          "Course Title": "Cultural Geography",
          "Location": "Geography Department"
        }
      ]
    },
    {
      "Date": "Thursday, May 16",
      "Time": "9:30 AM",
      "Courses": [
        {
          "Course Code": "BUS 301",
          "Course Title": "Strategic Management",
          "Location": "Business School"
        },
        {
          "Course Code": "PHIL 201",
          "Course Title": "Ethics",
          "Location": "Philosophy Department"
        }
      ]
    },
    {
      "Date": "Friday, May 17",
      "Time": "10:30 AM",
      "Courses": [
        {
          "Course Code": "LANG 202",
          "Course Title": "Spanish II",
          "Location": "Language Lab"
        },
        {
          "Course Code": "ANTH 301",
          "Course Title": "Anthropology of Globalization",
          "Location": "Anthropology Department"
        }
      ]
    }
  ]
}



school_fees_data = {
  "University Fees Table": [
    {
      "Item": "Tuition Fees",
      "Description": "Per credit hour for undergraduate courses",
      "Amount (NGN)": "₦90,000"
    },
    {
      "Item": "",
      "Description": "Per credit hour for graduate courses",
      "Amount (NGN)": "₦120,000"
    },
    {
      "Item": "Accommodation Fees",
      "Description": "Premium Hall (per semester)",
      "Amount (NGN)": "₦450,000"
    },
    {
      "Item": "",
      "Description": "Classic Hall (per semester)",
      "Amount (NGN)": "₦300,000"
    },
    {
      "Item": "Semester Fees",
      "Description": "Student Activity Fee (per semester)",
      "Amount (NGN)": "₦5,000"
    },
    {
      "Item": "",
      "Description": "Technology Fee (per semester)",
      "Amount (NGN)": "₦10,000"
    },
    {
      "Item": "",
      "Description": "Health Services Fee (per semester)",
      "Amount (NGN)": "₦7,500"
    },
    {
      "Item": "",
      "Description": "Library Fee (per semester)",
      "Amount (NGN)": "₦5,000"
    }
  ]
}

new_data = {
      "What type of halls are available to students in the main campus?": "We have Premium halls and classic halls for both male and female.",
      "How is hostel accommodation assigned to students?": "We offer both premium and classic halls, each designated for specific academic levels. Depending on your level and selected plan, students have the flexibility to choose the hall that best aligns with their preferences.",
}


answers = get_answered_enquiries()
enquiries_and_answer = [(e["enquiry"],e["answer"]) for e in answers]
new_data = new_data.update(dict(enquiries_and_answer))

print(enquiries_and_answer)
print(new_data)