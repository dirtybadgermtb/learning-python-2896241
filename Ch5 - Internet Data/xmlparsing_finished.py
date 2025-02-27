# 
# Example file for parsing and processing XML
# LinkedIn Learning Python course by Joe Marini
#


import xml.dom.minidom
import os

def main():
    # Get absolute path to the XML file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(current_dir, "samplexml.xml")
    
    try:
        # Parse the XML file
        doc = xml.dom.minidom.parse(xml_file)
        
        # Print document info
        print(doc.nodeName)
        print(doc.firstChild.tagName)
        
        # Get and print all skills
        skills = doc.getElementsByTagName("skill")
        print ("%d skills:" % skills.length)
        for skill in skills:
            print (skill.getAttribute("name"))
        
        # create a new XML tag and add it into the document
        newSkill = doc.createElement("skill")
        newSkill.setAttribute("name", "jQuery")
        doc.firstChild.appendChild(newSkill)

        skills = doc.getElementsByTagName("skill")
        print ("%d skills:" % skills.length)
        for skill in skills:
            print (skill.getAttribute("name"))
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()

