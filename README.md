# MatSci-LumEn: Materials Science Large Language Models Evaluation

## Formula matching 


### Evaluation

Evaluated on the 23/12/25

```
                  precision    recall  f1-score   support

        <doping>     0.6926    0.6377    0.6640       265
   <fabrication>     0.3333    0.0909    0.1429        44
       <formula>     0.8348    0.8459    0.8403      2569
          <name>     0.7346    0.7935    0.7629       949
         <shape>     0.9089    0.9608    0.9341       841
     <substrate>     0.5875    0.3176    0.4123       148
         <value>     0.8844    0.8920    0.8882       463
      <variable>     0.9645    0.9710    0.9677       448

all (micro avg.)     0.8321    0.8385    0.8353      5727
```

## Getting started

```shell
conda create --name lumen python=3.9
conda activate lumen 
```

```shell
pip install -r requirements.txt 
```