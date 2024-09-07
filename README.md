# DataParenting
A data pipeline that produces data nobody uses is a bill, not an asset!\
I play the bad-cop when it comes to hoarding.\
Do we need this data? For this long, at this place, in this manner? What if we do not have it?\
In this space, I deep-dive into how to ask and answer these questions, which in the end leads to an unregrettable decision, hopefully. 

![Booktalk - haely-2](https://github.com/haely/DataParenting/assets/32823897/a2a72629-2a7f-4356-911b-f814d6652978)

## How it all started
I was working on a hobby NLP project - models to detect slang words in the English language. The goal was to process the language exactly like humans do — *pragmatic* enough to get the slang and the occasional double negatives for a real negative, and *semantic* enough that it works for a lifetime.
But what do you do when the humans keep on changing the meaning of a word? More precisely, how do you deal with an ever-evolving and ever-changing language that goes from “I am up for it” to “I am down” in the same generation to mean literally the same thing that they would love to give it a try.

Most of our resources in academia and in industries to an extent go in creating that perfect model that will conquer it all — data glitches, seasonal trends, and even occasional inital misclassifications. Maybe it is time we apply the age old adage to Machine Learning — Consistency beats intensity.

A consistently improved process of preprocessing and cleaning is the next requirement in data science.

## Medium Articles

- [Data intro](#data-hoarding)
- [Cloud Storage](#cloud-storage)
- [Data Lifecycle](#data-lifecycle)
- [Data Drift](#data-drift)
- [Data Compression](#data-compression)
- [VertexAI](#vertex-ai)
---

## Data Lifecycle (how long in which storage tier?)

## Data Retention (if and when to delete?)
Does legal allow this?\n
Have I ever had to retireive it from any of my non-standard storage tiers?\n
Has it been 2xtime outside standard storage than inside standard storage?\n
DELETE!

## Data Compression (shall I, how?)
Usually large storage files need compression - iamges, videos etc\n
Compression is neither easy nor cheap. It takes time and effort to convert back and forth from original (eg mp4) to comrpessed (txt/bin etc) files.\n
Maybe compress before cold tier transfer?\n
Maybe alwsys compress if your de-comress method is not too lossy, too time consuming, or too complex.

## Cloud specific practices

### AutoClass

### Multi-regional
Do I need a deep-copy of my data in multiple regions?]\n
Is the cost of data transfer across regions (1 or 2 or n times) higher than my cost of keeping the data in multiple regions?

### Move to on-prem
If I frequently access data, if my data is large enough, cannot be compressed, and may or may not be edited, it might be finally time to intriduce your own private cloud aka old style on-prem storage. 

### Object size, numbers etc


\n
## Data Drift
An ML model in production may or may not be constantly re-trained to avoid unnecessary resource consumption. Whie most simpler use-cases will not see a difference in final results, some places might. Especially where data is slowly changing aka Data Drift.\n
e.g. A neural network predicting rainfall built in 2010s will need a fix to accomodate climate change.\n
or a language constantly evolving...

### Numerical data
For numerical data, a quick summary stats check on either data or results or both will tell you if the data drift is significant enough to need a model re-evaluation/re-train. This is not exactly an outlier check. It is more like - is my mean drifitng?\n
e.g. 10 years of data tells me mean temperature in January is 100', median is 95'...\n
if my new Jan mena temoerture is 98' and my new median is 93' --- strike 1\n
if my new Feb mena temoerture is old_mean-2 and my new median is old_mean-3 -- strike 2\n
if my new March mena temoerture is old_mean-3 and my new median is old_mean-3 -- strike 3\n
\n
Yes, temperature is slowly rising.\n
A z-score check, IQR check, standard deviation comparison will give a bigger picture on this.\n
\n

### Non-numerical data

TBD

## Data Hoarding
Don't be a Data Hoarder
### Link 
https://medium.com/@haely.shah/dont-be-a-data-hoarder-embrace-data-parenting-bf17d2cd0eda

## Cloud Storage
Cloud Storage needs Spring cleaning too!
### Link 
https://medium.com/@haely.shah/cloud-storage-spring-cleanup-what-to-sweep-under-the-rug-and-what-to-trash-00513f6cb386

## Data Lifecycle
Data Lifecycle - get started
### Link
https://medium.com/@haely.shah/the-data-lifecycle-where-does-your-data-live-and-for-how-long-1d87ad96289b

## Data Drift
Drift in Data can change your model results
### Link
https://medium.com/@haely.shah/data-drift-the-stealthy-threat-to-your-machine-learning-models-4dbe7b530497

## Data Compression
Lossy, lossless etc. how to manage this?
### Link
https://medium.com/@haely.shah/data-compression-shrink-your-data-footprint-without-shrinking-your-options-a13b9292fb1f
 
## Vertex AI






