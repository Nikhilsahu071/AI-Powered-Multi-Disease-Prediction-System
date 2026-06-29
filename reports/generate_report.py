from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(name, age, gender, prediction, confidence, recommendation):

    doc = SimpleDocTemplate("reports/Health_Report.pdf")

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Multi Disease Prediction Report</b>", styles["Title"]))

    story.append(Paragraph(f"Patient Name : {name}", styles["BodyText"]))
    story.append(Paragraph(f"Age : {age}", styles["BodyText"]))
    story.append(Paragraph(f"Gender : {gender}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"Prediction : {prediction}", styles["BodyText"]))
    story.append(Paragraph(f"Confidence : {confidence}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Recommendation</b>", styles["Heading2"]))

    story.append(Paragraph(recommendation, styles["BodyText"]))

    doc.build(story)

    return "reports/Health_Report.pdf"