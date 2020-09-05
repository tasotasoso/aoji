![UT by github action](https://github.com/tasotasoso/aoji/workflows/Python%20package/badge.svg)

# Aoji

Aoji supports createing your local git project for kaggle.

Your kaggle projects will travel kaggle cloud to your local PC to your github repositry.

Let's create your kaggle project at your local environment by aoji.

# Usage

1. Clone and install aoji.
<pre>
git clone https://github.com/tasotasoso/aoji
cd aoji
python setup.py install
</pre>

2. Set your API credentioals for kaggle.
You have to create and set API Token ofr kaggle.
In detail, check Kaggle API git repositry.
https://github.com/Kaggle/kaggle-api#api-credentials 

3. launch your project.
Launch python shell and launch your project.
<pre>
import aoji
aoji.launch()
</pre>

# Note

Aoji includes source reffering to kaggle API source code.

This code subject to the it's Apache-2.0 license.

