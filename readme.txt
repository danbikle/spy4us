/home/ann/spy4us/readme.txt

The files in this repo are part of an effort to predict one day percent gain of the S&P 500.

I call this application 'spy4.us' because the stockmarket provides an ETF named SPY.

So if I can predict gains of the S&P 500, a good way to act on those
predictions is to buy/sell SPY in my brokerage account.

The software in this repo is divided into two parts.

The first part calculates the predictions from prices of SPY.

The second part copies the predictions to a meteor application.

Then I rely on meteor.com to serve the predictions to you when you
want to see them in your browser.

Questions?

e-me: dan@bot4.us

-- Dan Bikle

Maybe you want to run this software on your laptop?

Installation Instructions:

- Install Linux Ubuntu 14 somewhere

- Login as root

- apt-get install gitk wget

- useradd -m -s /bin/bash ann

- passwd ann

- ssh ann@yourhost

- wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.2.0-Linux-x86_64.sh

- bash Anaconda3-2.2.0-Linux-x86_64.sh

- mv ~ann/anaconda3/bin/curl ~ann/anaconda3/bin/curl_ana

- git clone https://github.com/danbikle/spy4us.git

- cat ~ann/spy4us/sitename_readme.txt

- vi  ~ann/spy4us/sitename.txt

- Create account on meteor.com

- curl https://install.meteor.com/ | sh

- ~ann/spy4us/call_ml101.bash

- Use a browser to look at your site on meteor.com

- Use a browser to look at my site: spy.meteor.com

- Ask questions:

dan@bot4.us

-- Dan Bikle
