{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import requests\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "url = (\"https://financialmodelingprep.com/api/v3/historical-price-full/index/%5EGSPC?apikey=b79521d0a15483a6c556d71f892d0be4\")\n",
    "\n",
    "def get_sp500_daily():\n",
    "    sp500daily = requests.get(url)\n",
    "    sp500daily = sp500daily.json()\n",
    "    sp500daily = sp500daily['historical']\n",
    "    sp500_d_change = pd.DataFrame.from_dict(sp500daily)\n",
    "    sp500_d_change.set_index('date', inplace = True)\n",
    "    columns =['change','high', 'adjClose', 'volume', 'open', 'label','low','unadjustedVolume', 'vwap','changeOverTime', 'close']\n",
    "    sp500_d_change = sp500_d_change.drop(columns, axis=1)\n",
    "    sp500_d_change.rename(columns = { 'changePercent' : 'change%'}, inplace = True)\n",
    "    sp500_d_change.to_csv('./sp500_daily_returns.csv')\n",
    "    return sp500_d_change\n",
    "\n",
    "def get_sp500_monthly():    \n",
    "    sp500monthly = requests.get(url)\n",
    "    sp500monthly = sp500monthly.json()\n",
    "    sp500monthly = sp500monthly['historical']\n",
    "    sp_m_change = pd.DataFrame.from_dict(sp500monthly)\n",
    "    columns =['change','high','label','low','unadjustedVolume', 'vwap','changeOverTime', 'close']    \n",
    "    sp_m_change = sp_m_change.drop(columns, axis=1)\n",
    "    sp_m_change.rename(columns = {'adjClose' : 'close', 'changePercent' : 'change%'}, inplace = True)\n",
    "    sp_m_change.set_index('date', inplace=True)\n",
    "    sp_m_change.index = pd.to_datetime(sp_m_change.index)\n",
    "    sp_m_change = sp_m_change.resample('1M').mean()\n",
    "    sp_m_change.to_csv('./sp500_monthly_returns.csv')    \n",
    "    return sp_m_change\n",
    "\n",
    "def get_sp_data():     \n",
    "    get_sp500_daily()\n",
    "    get_sp500_monthly()\n",
    "    return\n",
    "\n",
    "get_sp_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
