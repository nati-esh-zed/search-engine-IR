import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

# Full corpus
corpus = [
    "Enhancing properties of bioplastic films.",
    "Current status of delnido cardioplegia.",
    "Existential study on Anthony Doerr's 'All the Light We Cannot See'.",
    "Comparative study on Kafka's and Roy's works.",
    "Autopsy study on coronary atherosclerosis.",
    "Research on neural correlates of consciousness.",
    "Examination of various English literary works.",
    "Studies on medical advancements.",
    "Contributions from researchers across disciplines.",
    "Responses to environmental stressors.",
    "Increased frequency of extreme wildfires.",
    "Farming as a tool for climate change mitigation.",
    "Recruitment notices for various scientific positions.",
    "AI's role in detecting hallucinations in language models.",
    "Economic impacts of public investments in AI.",
    "Innovations for a net-zero future in oil refineries.",
    "The state of hiring researchers in science.",
    "Combating hallucinations in large language models.",
    "Exoskeleton assistance via learning in simulation.",
    "Tracking economic impacts of AI investments.",
    "Innovations in net-zero oil refineries.",
    "Recruitment for synthetic biology and medical research positions.",
    "Developments in machine learning.",
    "Advances in generalizing language models.",
    "Better diagnostic methods via AI.",
    "Ethical implications of AI in healthcare.",
    "AI's role in detecting alien biochemistries.",
    "Studies on environmental stress responses.",
    "Advances in coral reef restoration techniques.",
    "Impact of climate change on local environments.",
    "Enhancements in bioplastic film properties.",
    "Neurological studies on consciousness and perception.",
    "Comparative literary analyses.",
    "Medical research on coronary atherosclerosis.",
    "Innovations in cardiac surgery techniques.",
    "The concept of the brain's 'reality threshold'.",
    "Theories on the emergence of consciousness.",
    "Challenges to the serotonin deficiency model of depression.",
    "Differentiation between depression and loneliness.",
    "High-profile collaboration on consciousness theories.",
    "Impacts of hallucinations on perceptions.",
    "Role of sensory experiences in consciousness.",
    "Advancements in understanding mental health.",
    "Neuroscientific insights on social isolation.",
    "Insights into brain communication with advanced imaging technology.",
    "Development of a low-cost flu test using CRISPR.",
    "Study on care following nonfatal overdoses.",
    "Stroke detection via smartphone screening tools.",
    "The role of the gut microbiome and brain activity in resiliency.",
    "Detailed examination of climate change impacts on local environments.",
    "Exploration of mild pain infliction for charitable fundraising.",
    "The potential of coral gyms to combat coral bleaching.",
    "AI model to detect alien life.",
    "The relationship between neural activity and cognitive resilience.",
    "Discovery of exoplanets in orbital resonance.",
    "Artificial intelligence developed to find alien life.",
    "New methods to restore coral reefs.",
    "Novel research on the neural correlates of consciousness.",
    "Breakthroughs in bioplastic film properties.",
    "Advancements in delnido cardioplegia for cardiac surgery.",
    "Study on the authenticity amidst adversity.",
    "Comparative analysis of Kafka's 'Metamorphosis' and Roy's 'The Folded Earth'.",
    "Coronary atherosclerosis autopsy study."
]

def preprocess(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

processed_corpus = [preprocess(doc) for doc in corpus]
