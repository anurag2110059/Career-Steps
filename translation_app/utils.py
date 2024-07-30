# utils.py

def analyze_text(text):
    # List of keywords related to different career paths
    career_keywords = {
        'technology': ['tech', 'programming', 'coding', 'computer', 'software'],
        'medicine': ['medical', 'doctor', 'nurse', 'healthcare', 'hospital'],
        'business': ['business', 'entrepreneur', 'management', 'finance', 'startup'],
        'art': ['art', 'creative', 'design', 'painting', 'music'],
        'engineering': ['engineering', 'mechanical', 'civil', 'electrical', 'design'],
        'sports': ['running', 'playing', 'yoga', 'cricket', 'hockey'],
        'hotel_management':['cook','food','chef']
        # Add more categories and keywords as needed
    }

    # Count occurrences of each keyword in the text
    keyword_counts = {career: sum(text.lower().count(keyword) for keyword in keywords) 
                      for career, keywords in career_keywords.items()}

    # Identify the career with the highest keyword count
    predicted_career = max(keyword_counts, key=keyword_counts.get)

    return predicted_career
