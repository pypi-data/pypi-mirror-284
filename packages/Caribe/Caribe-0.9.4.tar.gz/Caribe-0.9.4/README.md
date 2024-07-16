
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Downloads](https://pepy.tech/badge/caribe)](https://pepy.tech/project/caribe) ![PyPI](https://img.shields.io/pypi/v/Caribe)[![Transformer](https://img.shields.io/badge/Transformer-T5-blue.svg)](https://huggingface.co/docs/transformers/model_doc/t5) [![Pandas](https://img.shields.io/badge/Pandas-1.3.4-green.svg)](https://pandas.pydata.org/) [![AI](https://img.shields.io/badge/AI-Artifical_Intelligence-blue.svg)]() [![Transformers](https://img.shields.io/badge/Transformers-4.15.0-blue.svg)](https://huggingface.co/) [![happytransformers](https://img.shields.io/badge/happytransformers-2.4.0-blue.svg)](https://happytransformer.com/) [![Python 3+](https://img.shields.io/badge/python-3+-blue.svg)]() [![NLP](https://img.shields.io/badge/nlp-natural_language_processing-blue.svg)]() [![T5-KES](https://img.shields.io/badge/T5-T5_KES-red.svg)](https://huggingface.co/KES/T5-KES) [![T5-TTParser](https://img.shields.io/badge/T5-TTParser-aqua.svg)](https://huggingface.co/KES/T5-TTParser) [![T5-Caribe-Capitalise](https://img.shields.io/badge/T5-Caribe_Capitalization-teal.svg)](https://huggingface.co/KES/caribe-capitalise) [![T5-TEC-ENG](https://img.shields.io/badge/T5-TEC_ENG-brown.svg)](https://huggingface.co/KES/TEC-English)

<p align="center">
<img src="https://github.com/KestonSmith/CaribeLogo/raw/master/CaribeLOGO.png" title="Caribe">








# Caribe 


>This is a natural processing python library takes Caribbean English Creoles and converts it to Standard English.
Future updates would include the conversion of other Caribbean English Creole languages to Standard English and additional natural language processing methods.

____

## Installation
  
Use the below command to install package/library
```
pip install Caribe 

```
____
## Visit the website: <a href="https://www.thecaribe.org/">here</a> 
---
## Main Usage
- ### Trinidad English Creole to English
```python

import Caribe as cb

text= "Dem men doh kno wat dey doing wid d money bai"

output= cb.tec_translator(text)

print(output.tec_translate()) #Output: These men do not know what they are doing with the money.


```
- ### English to Trinidad English Creole 
```python

import Caribe as cb

text= "Where are you going now?"

output= cb.english_to_tec(text)

print(output.translate()) #Output: Weh yuh going now


```
- ### Guyanese English Creole to English
```python
from Caribe import guyanese as gy

text= "Me and meh kozn waan ah job"

output= gy.gec_translator(text)

print(output.gec_translate()) #Output: Me and my cousin want a job.


```
____
 ## Other Usages
 > Sample 1: Checks the english creole input against existing known creole phrases before decoding the sentence into a more standardized version of English language. A corrector is used to check and fix small grammatical errors.
```python
# Sample 1
import Caribe as cb


sentence = "Dey have dey reasons"
standard = cb.phrase_decode(sentence)
standard = cb.trinidad_decode(standard)
fixed = cb.caribe_corrector(standard)
print(fixed) #Output: They have their reasons.

```
>Sample 2: Checks the trinidad english creole input against existing known phrases
```python
# Sample 2 
import Caribe as cb


sentence = "Waz de scene"
standard = cb.phrase_decode(sentence)

print(standard) # Outputs: How are you

```
>Sample 3: Checks the sentence for any grammatical errors or incomplete words and corrects it.
```python
#Sample 3
import Caribe as cb


sentence = "I am playin fotball outsde"
standard = cb.caribe_corrector(sentence)

print(standard) # Outputs: I am playing football outside

```
>Sample 4: Makes parts of speech tagging on creole words.
```python
#Sample 4
import Caribe as cb

sentence = "wat iz de time there"
analyse = cb.nlp()
output = analyse.caribe_pos(sentence)

print(output) # Outputs: ["('wat', 'PRON')", "('iz', 'VERB')", "('de', 'DET')", "('time', 'NOUN')", "('there', 'ADV')"]

```
>Sample 5: Remove punctuation marks.
```python
#Sample 5
import Caribe as cb

sentence = "My aunt, Shelly is a lawyer!"
analyse = cb.remove_signs(sentence)


print(analyse) # Outputs: My aunt Shelly is a lawyer

```

>Sample 6: Sentence Correction using T5-KES.
```python
#Sample 6 Using t5_kes_corrector
import Caribe as cb


sentence = "Wat you doin for d the christmas"
correction = cb.t5_kes_corrector(sentence)


print(correction) # Output: What are you doing for christmas?

```
>Sample 7: Sentence Correction using Decoder and T5-KES.
```python
#Sample 7 Using t5_kes_corrector and decoder
import Caribe as cb


sentence = "Ah want ah phone for d christmas"
decoded= cb.trinidad_decode(sentence)
correction = cb.t5_kes_corrector(decoded)


print(correction) # Output: I want a phone for christmas.

```

>Sample 8: Sentence Capitalisation.
```python
#Sample 7 Using Caribe sentence capitalization model
import Caribe as cb


sentence = "john is a boy. he is 12 years old. his sister's name is Joy."

capitalized_text= cb.capitalize(sentence)

print(capitalized_text) # Output: John is a boy. He is 12 years old. His sister's name is Joy.

```

---
- ## Additional Information
    - `trinidad_decode()` : Decodes the sentence as a whole string.
    - `guyanese_decode()`:  Decodes the sentence as a whole string.
    - `trinidad_decode_split()`: Decodes the sentence word by word.
    - `phrase_decode()`: Decodes the sentence against known creole phrases.
    - `caribe_corrector()`: Corrects grammatical errors in a sentence using a trained NLP model.
    - `t5_kes_corrector()`: Corrects grammatical errors in a sentence using a trained NLP model.
    - `trinidad_encode()`: Encodes a sentence to Trinidadian English Creole.
    - `guyanese_encode()`: Encodes a sentence to Guyanese English Creole.
    - `trinidad_direct_translation()`: Translates Trinidad English Creole to English.
    - `capitalize()`: Capitalize groups of sentences using an NLP model.
    - `caribe_pos()`: Generates parts of speech tagging on creole words.
    - `pos_report()`: Generates parts of speech tagging on english words.
    - `remove_signs()`: Takes any sentence and remove punctuation marks. 

---
- ## File Encodings on NLP datasets
Caribe introduces file encoding (Beta) in version 0.1.0. This allows a dataset of any supported filetype to be translated into Trinidad English Creole. The file encoding feature only supports txt, json or csv files only.

- ### Usage of File Encodings:
```python
import Caribe as cb

convert = cb.file_encode("test.txt", "text")
# Generates a translated text file
convert = cb.file_encode("test.json", "json")
# Generates a translated json file
convert = cb.file_encode("test.csv", "csv")
# Generates a translated csv file


```
---
- ## First Parser for the Trinidad English Creole Language

This model utilises T5-base pre-trained model. It was fine tuned using a combination of a custom dataset and creolised JFLEG dataset. JFLEG dataset was translated using the file encoding feature of the library. 

Within the Creole continuum, there exists different levels of lects. These include: 

- Acrolect: The version of a language closest to standard international english.
- Mesolect: The version that consists of a mixture of arcolectal and basilectal features.
- Basilect: The version closest to a Creole language.

**This NLP task was difficult because the structure of local dialect is not standardised but often rely on the structure of its lexifier (English). Spelling also varies from speaker to speaker. Additionally, creole words/spelling are not initial present in the vector space which made training times and optimization longer .**

## Results
Initial results have been mixed.

| Original Text                            | Parsed Text                         | Expected or Correctly Parsed Text   |
|------------------------------------------|-------------------------------------|-------------------------------------|
| Ah have live with mi paremnts en London. | Ah live with meh parents in London. | Ah live with meh parents in London. |
| Ah can get me fone?                      | Ah cud get meh fone?                | Ah cud get meh fone?                |
| muh moda an fada is nt relly home        | muh moda an fada is nt relly home.  | muh moda an fada not really home.    |
| Me ah go market                     | Ah going tuh d market.             | Ah going tuh d market. / I going tuh de market.           |
| Ah waz a going tu school.                | Ah going to school.                 | Ah going to school.                 |
| Ah don't like her.                          | Ah doh like she.                   | Ah doh like she. / I doh like she. |
| Ah waz thinking bout goeng tuh d d Mall. | Ah thinking bout going tuh d Mall.  | Ah thinking bout going tuh d mall.  |


### Usage of the TrinEC Parser

```python
import Caribe as cb

text= "Ah have live with mi paremnts en London"

s= cb.Parser(text)

print(s.TT_Parser()) #Output: Ah live with meh parents in London.


```
---
## Trinidad English Creole to English Translator using the T5 model
A model was fine-tuned(supervised) on a custom dataset to translate from Trinidad English Creole to English. This task was done as an alternative method to the decoded dictionary- sentence correction method. Future Testing will illustrate a comparison between both methods.

```python
import Caribe as cb

text= "Dem men doh kno wat dey doing wid d money bai"

output= cb.tec_translator(text)

print(output.tec_translate()) #Output: These men do not know what they are doing with the money.


```

---
## Dictionary Data
The encoder and decoder utilises a dictionary data structure. The data for the dictionary was gathered from web-scapping social media sites among other websites and using Lise Winer Dictionary of the English Creole of Trinidad and Tobago among other scholarly resources.
____
## Fine-tune a T5 model on custom datasets easier using Caribe built on HuggingFace Transformers APIs 

### Training Section:
Caribe allows any user to fine-tune a T5 model on a custom dataset.  The snippet below trains and generates a model in the "model/" folder. 
Please ensure that your training and evaluation datasets are in the recommended format before training. For more info checkout [T5 documentation.](https://huggingface.co/docs/transformers/main/en/model_doc/t5#t5) 
```python
from Caribe import T5_Caribe as t5

model = t5.T5_Trainer("train_dataset.csv", "eval_dataset.csv")
connect = model.connect_datasets("csv")
train = model.caribe_training(output_path="./content", epochs=10, eval_strategy="steps", decay=0.01, l_rate=2e-5, train_batch_size=8, eval_batch_size=8, checkpoints=2)

```
### Parameters:
 - Epochs : Num of training iterations.

 - eval_strategy: Displays training in 'steps' or 'epoch'
 - decay: Regularization of Training weights.

 - l_rate: Learning rate.

 - train_batch_size: Number of samples from the training data per iteration.

 - eval_batch_size: Number of samples from the evaluation data per iteration.

 - checkpoints: Produces and saves preset amount of model versions during training.

 ### Generating Text Section:
 Generates text from the output of the model.  Please note that if you have not train and generate the model folder or have a pre-existing model folder with the required files, the below code will generate an error.
 ```python
from Caribe import caribe_generate

g = caribe_generate.generate_text("eng:How are you", temperature=1.7, num_beams=10)
output=g.output()
print(output)

 ```
### Parameters:
- min_length: Minimum number of generated tokens.

- max_length:Max number of generated tokens.

- do_sample: When True, picks words based on their conditional probability.

- early_stopping: If true,stops the beam search when the least amount of num beams sentences have been completed each batch.

- num_beams: Number of steps for each search path.

- temperature: The value utilized to calculate the likelihood of the next token.

- top_k:The tokens with the greatest likelihood should be retained for top-k sampling.

- top_p:  Most tokens with the highest probabilities that add up to top_p or higher.

- no_repeat_ngram_size: The amount of times an n-gram that size can only occur once. 

---
## Caribe_Corrector (T5-KES) vs Gingerit Corrector
Initial Tests were carried out with performance factors to measure the accuracy of the correction and the degree of sentence distortion from the correct sentence. Initial tests showed that the T5 corrector performed better in terms of accuracy with a lower sentence distortion and attained higher MT scores. The T5 corrector also outperforms Gingerit on positional translations as shown in the table below.

| **Original Creole Text**         | **Decoded Sentence**               | **Caribe Corrector (T5-KES)**       | **Gingerit Corrector**              | **Correct Output**                  |
|----------------------------------|------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|
| Ah need ah car fuh meh birthday  | I need I car for me birthday       | I need a car for my birthday.       | I need my car for my birthday       | I need a car for my birthday        |
| Wah iz d time on yuh side?       | want is the time on you side?      | What is the time on your side?      | Want is the time on your side?      | What is the time on your side?      |
| Ah man is d provider of de house | I man is the provider of the house | A man is the provider of the house. | My man is the provider of the house | A man is the provider of the house. |
| Ah orange issa fruit             | I orange is a fruit                | An orange is a fruit.               | My orange is a fruit                | An orange is a fruit.               |
| Wah time yuh wah come over?      | want time you want come over?      | What time do you want to come over? | Want time you want to come over?    | What time do you want to come over? |
|Dey make dey own choices at the end of de day  |their make their own choices at the end of the day |They make their own choices at the end of the day. |they make their own choices at the end of the day. |They make their own choices at the end of the day. |

---
# Guyanese English Creole Features
Caribe introduces decoding, encoding and file encoding using Guyanese English Creole and translating Guyanese dialect. 


## Guyanese English Creole to English
```python
from Caribe import guyanese as gy

text= "Me and meh kozn waan ah job"

output= gy.gec_translator(text)

print(output.gec_translate()) #Output: Me and my cousin want a job.


```

- ### Decoding a sentence
```python
# Decoding a creole sentence

from Caribe import guyanese as gy

sentence = "waam star, me ga fu go di markit"
output = gy.guyanese_decode(sentence)
print(output) # Output: what going on brother, me have to go the market

```
- ### Encoding a sentence
```python
# Encoding a sentence

from Caribe import guyanese as gy

sentence = "I do not want nothing to do with him"
output = gy.guyanese_encode(sentence)
print(output) # Output: ah du not waan notn tuh du wid him
```

- ### File Encodings on NLP datasets using Guyanese English Creole:
```python
from Caribe import guyanese as gy

convert = gy.guyanese_file_encode("test.txt", "text")
# Generates a translated text file
convert = gy.guyanese_file_encode("test.json", "json")
# Generates a translated json file
convert = gy.guyanese_file_encode("test.csv", "csv")
# Generates a translated csv file
```

---
# News, Issues and Future Plans (14/08/2022)

- Datasets are continuously being updated.
- NLP Models and Dictionaries are continuously updated.
- Future plans to create translations, models and datasets for Caribbean French and Spanish Creoles to their respective lexifers (Requires extensive research).
- Some users complained of problems importing some of the dependencies. This is currently being monitored (10/06/2022).
- New model introduced for sentence capitalization (09/06/2022) !!!
- NEW model introduced for direct translation from Trinidad English Creole(TEC) to English(26/06/2022).
- NEW model introduced for direct translation from Guyanese English Creole(GEC) to English(26/09/2022).

- The gingerit_corrector function is deprecated. 

---
- ## Contact 
For any concerns or issues with this library.

Email: keston.smith@my.uwi.edu 

Website: https://www.thecaribe.org/
___