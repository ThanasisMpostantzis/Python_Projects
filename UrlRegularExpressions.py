#Το παρακάτω πρόγραμμα γραμμένο σε python παίρνει ως είσοδο ένα URl και αναγνωρίζει μέσω κανονικών
#εκφράσεων τα παρακάτω ζητούμενα:
#α) Αν η ιστοσελίδα αφορά ένα συνέδριο, και αν η απάντηση είναι καταφατική, τότε επίσης και τα εξής: 
#β) Ποιο είναι το χρονικό διάστημα που θα διεξαχθεί το συνέδριο
#γ) Ποιος είναι ο τόπος διεξαγωγής
#δ) Ποιο το κόστος συμμετοχής για διάφορες κατηγορίες συμμετεχόντων
#ε) Ποιο το αντικείμενο του συνεδρίου
#Ειδικά για το α, η απάντηση μπορεί να βασιστεί στην ύπαρξη ή μη της λέξης conference στον τίτλο
#της σελίδας.

import re
import requests

url = input("Παρακαλώ δώστε το URL: ")

response = requests.get(url)
html_content = response.text

if response.status_code != 200:
    print("Σφάλμα κατά τη λήψη της ιστοσελίδας.")
    exit()

if "conference" in html_content.lower():
    answer = input("Η ιστοσελίδα αφορά συνέδριο; Ναι ή Όχι; ")
    if answer.lower() == "ναι":
        date_pattern = r'(\d+\s\-\s\d+\s\w+\s\d{4})'
        location_pattern = r'Location:</strong>\s*<span class="event-loc">(.*?)</span>'
        fee_pattern = r'Price:</strong>(.*?)<br>'
        topic_pattern = r'<h1 class="event-title">(.*?)</h1>'
        
        date_match = re.search(date_pattern, html_content)
        location_match = re.search(location_pattern, html_content)
        fee_match = re.search(fee_pattern, html_content)
        topic_match = re.search(topic_pattern, html_content)

        if date_match:
            date = date_match.group(1).strip()
            print("Το συνέδριο θα διεξαχθεί στις:", date)
        else:
            print("Δεν μπορεί να βρεθεί η ημερομηνια")
            
        if location_match:
            location = location_match.group(1).strip()
            print("Η τοποθεσία του συνεδρίου θα είναι στην", location, "τοποθεσία")
        else:
            print("Δεν μπορεί να βρεθεί η τοποθεσία")
            
        if fee_match:
            fee = fee_match.group(1).strip()
            print("Tο κόστος συμμετοχής για διάφορες κατηγορίες συμμετεχόντων είναι: ", fee)
        else:
            print("Δεν μπορεί να βρεθεί ο φόρος")
            
        if topic_match:
            topic = topic_match.group(1).strip()
            print("Το αντικείμενο του συνεδρίου είναι: ", topic)
        else:
            print("Δεν μπορεί να βρεθεί το αντικείμενο του συνεδρίου")
    else:
        print("Η ιστοσελίδα δεν αφορά συνέδριο")
else:
    print("Δεν μπορούν να βρεθούν πληροφορίες")
        


