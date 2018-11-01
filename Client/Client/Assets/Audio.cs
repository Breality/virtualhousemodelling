
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Windows.Speech;

public class Audio : MonoBehaviour
{

    // Use this for initialization
    private KeywordRecognizer keywordRecognizer;
    string[] key_words = new string[] {
        "Door", "Archive", "Globe", "Sofa", "Sabine", "Castillo", "Hannon", "Brandt", "Point", "Bay", "Crisfield", "Machine", "Warrington", "Paterson", "Turquoise",
        "Beige/Red", "Kathleen", "Cimarron", "Stainless", "Beige/Pink", "Keane", "Chan", "Adjustable", "Arianna", "Clair", "Shaker", "Brook",
        "Chesterfield", "Settee", "Etagere", "LED", "Arms", "Mullenax", "Microscopium", "Glam", "in", "Sowerby", "Square", "Stoneford", "Lockwood",
        "Hand", "Decatur", "Selzer", "Silvis", "Haleakal", "Cleland", "Modern", "Croydon", "Neil", "Kaitlin", "Maria", "Upholstery",
        "Leisure", "Boothby", "Auden", "Gammons", "Quintus", "Tucson", "Multi", "Martinique", "Haywood", "Ellisville", "Cubicals", "Skirted", "Mid-Back",
        "Colleen", "Anissa", "Mathis", "Aliyah", "Side", "Fitzhugh", "Sirine", "Global", "Mid", "Whiteabbey", "Ricardo", "Forteau", "Virginia", "Hobgood",
        "Dual", "Nobles", "Ivory/Silver", "Simmons", "Leaf", "Fortville", "Kitchen", "Paisley", "Hand-Braided", "Barkell", "Upholstered", "Cangelosi", "Weare",
        "Norfolk", "Sleeper", "Gennevilliers", "Block", "Hattiesburg", "Brassiewood", "Balderston", "Ivy", "Evangeline", "Cainsville", "Keystone", "Extendable",
        "Harrison", "Glass", "Unit", "Gentry", "Floral", "Ivory", "Storage", "Randall", "Round", "Nunley", "Tile", "Rectangular", "Luther", "Treece", "Wooden",
        "Janeen", "Island", "Cocktail", "Solid", "Yerres", "Swivel", "Smithtown", "Metal", "Loveseat", "Wingback", "Blue", "Fresnay", "Armchair", "Liam", "Evadne",
        "Natuna", "Lift", "Beige/Green", "Spiral", "Lester", "Kimbell", "Scipio", "Ivory/Fuchsia", "Millicent", "Marble", "Birmingham", "Ottoman", "Harding", "Chair",
        "Steel", "Dining", "Faux", "Cube", "Boulton", "Creeksville", "Lorraine", "Carrion", "Burton", "Alijah", "Barrel", "Gray", "and", "Royal", "Altitude", "Mcguire",
        "Radiance", "Indoor", "Pillow", "Ceramic", "Lago", "Donohoe", "Woven", "Table", "Rockville", "with", "Indira", "Farmingdale", "Colston", "Weymand", "Kaiser",
        "Jerlene", "Harper", "Kier", "Geometric", "Baffin", "Alvarado", "Keanu", "Drawer", "Top", "Warm", "Ewenn", "Wylie", "Derrico", "Oxendine", "Chrysanthos",
        "Lantern", "Palm", "Navy", "Back", "Captains", "Kistler", "Edison", "Bella", "Borlon", "Zainab", "Tufted", "Garner", "Leather", "Ladder", "Oridatown",
        "Spirit", "Colborne", "Valley", "Darchelle", "Joseph", "Goodyear", "Sterling", "Smith", "Shapes", "Wood", "Benedetto", "Leaves", "Stools", "Sigler", "Vintage", "Groner", "Beach", "Athenis", "Raffin", "Contemporary", "With", "Drayton", "Parksley", "Quinten", "Set", "Terrarium", "Santa", "Grimes", "Trunk", "Sydnor", "Drop", "Valerie", "Avery", "Shade", "Aldridge", "Yellowstone", "Dark", "Lundgren", "Giana", "Wasser", "Marta", "Dewitt", "Potts", "Deluxe", "Arm", "Clarence", "Lamp", "Swirl", "Bohl", "Beige/Brown", "Modular", "Fortunat", "Traditional", "Craig", "Light", "Groveland", "Annable", "Century", "Finnur", "Pink", "Cremorne", "Shounak", "Malcolm", "White", "Coffee", "Bookcase", "Cart", "Arcs", "Slipper", "End", "Convertible", "Coggin", "Alfredo", "Leesburg", "Fortuna", "Lake", "Huntsville", "Standard", "Dyer", "Desk", "Seguin", "Area", "Lounge", "Zoller", "Parsons", "Myia", "Bowerbank", "Rutherford", "Drum", "Cage", "Domenica", "Crow", "Krol", "Sheryl", "Big", "Ermont", "Marcelo", "Dorset", "Achilles", "Salazar", "Blakesley", "Fabric", "Casas", "Evanston",
        "Del", "Affric", "Harbison", "Melmore", "Gehl", "Alejandro", "Grey", "Kellie", "Butcher", "Ares", "Pouf", "Gage", "Bergh", "Rug", "Swing" };

    public Storage storageHolder;
    public main gameHandler;

    [SerializeField]
    private Text m_Hypotheses;


    [SerializeField]
    private Text m_Recognitions;

    private DictationRecognizer m_DictationRecognizer;

    void Start()
    {
        m_DictationRecognizer = new DictationRecognizer();

        m_DictationRecognizer.DictationResult += (text, confidence) =>
        {
            Debug.LogFormat("Dictation result: {0}", text);
            try
            {
                m_Recognitions.text += text + "\n";
            }
            catch
            {
                Debug.Log("Problems, problems, problems");
            }

            string best_match = "";
            foreach (string word in text.Split(new char[] { ' ' }))
            {
                string correctWord = word[0].ToString().ToUpper() + word.Substring(1);
                if (key_words.Contains(correctWord) && correctWord.Length > best_match.Length)
                {
                    best_match = correctWord;
                }
                else if (new string[] { "Place", "Cancel", "Rotate", "Move", "Destroy" , "Email" }.Contains(correctWord))
                {
                    gameHandler.Command(correctWord);
                }
            }

            Debug.Log(best_match);
            if (best_match.Length > 0)
            {
                foreach (KeyValuePair<string, Dictionary<string, string>> entry in storageHolder.items)
                {
                    if (entry.Key.Contains(best_match))
                    {
                        gameHandler.newSelection(entry.Key);
                        break;
                    }
                }
            }
        };

        m_DictationRecognizer.DictationHypothesis += (text) =>
        {
            //Debug.LogFormat("Dictation hypothesis: {0}", text);
            try
            {
                m_Hypotheses.text += text;
            }
            catch
            {
                Debug.Log("Problems taking place");
            }

        };

        m_DictationRecognizer.DictationComplete += (completionCause) =>
        {
            // if (completionCause != DictationCompletionCause.Complete)
            //Debug.LogErrorFormat("Dictation completed unsuccessfully: {0}.", completionCause);
        };

        m_DictationRecognizer.DictationError += (error, hresult) =>
        {
            //Debug.LogErrorFormat("Dictation error: {0}; HResult = {1}.", error, hresult);
        };

        m_DictationRecognizer.Start();
    }


    // Update is called once per frame
    void Update()
    {

    }
}
