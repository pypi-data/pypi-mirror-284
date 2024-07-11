# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:21:17 2024

@author: JulianReul
"""

import numpy as np

class Mechanism():
    
    """
    The class Mechanism describes any functionality associated with
    a theoretical derivative of the H2Global mechanism.
    """
    
    def __init__(self,
                 purchase_price,
                 sales_price,
                 subsidy_period,
                 subsidy_volume,
                 **kwargs
                 ):
        
        #Initialize object attributes
        self.ATTR = {}
        
        #Required arguments
        self.ATTR["SUBSIDY_PERIOD"] = subsidy_period
        self.ATTR["SUBSIDY_VOLUME"] = subsidy_volume
        
        #____Define the number of stochastic scenarios
        self.ATTR["NUMBER_SCENARIOS"] = kwargs.get("NUMBER_SCENARIOS", 1000)

        # ____Define the value of volatility for sales price
        self.ATTR["VOLATILITY"] = kwargs.get("VOLATILITY", 0)

        if isinstance(purchase_price, int) or isinstance(purchase_price, float):
            self.ATTR["PURCHASE_PRICE"] = np.array([purchase_price for i in range(subsidy_period)])
        elif isinstance(purchase_price, list):
            if len(purchase_price) == subsidy_period:
                self.ATTR["PURCHASE_PRICE"] = np.array(purchase_price)
            else:
                raise AttributeError("Length of array -purchase_price- does not equal funding period.")
        elif isinstance(purchase_price, np.ndarray):
            shape_array = purchase_price.shape
            dim_array = purchase_price.ndim
            if dim_array == 1:
                if shape_array[0] == subsidy_period:
                    PURCHASE_PRICE_ARRAY_2D = purchase_price[:, np.newaxis]*np.ones(self.ATTR["NUMBER_SCENARIOS"])
                    self.ATTR["PURCHASE_PRICE"] = PURCHASE_PRICE_ARRAY_2D
                else:
                    raise AttributeError("Length of array -purchase_price- does not equal funding period.")
            elif dim_array == 2:
                if shape_array[0] == subsidy_period and shape_array[1] == self.ATTR["NUMBER_SCENARIOS"]:
                    self.ATTR["PURCHASE_PRICE"] = purchase_price
                else:
                    raise AttributeError("Dimensions of array -purchase_price- do not fit definitions for period and simulated scenarios.")
            else:
                raise AttributeError("Dimensions of array -purchase_price- must be 1 or 2.")
        else:
            raise AttributeError("Unknown input format for attribute -purchase_price-")
        
        if isinstance(sales_price, int) or isinstance(sales_price, float):
            self.ATTR["SALES_PRICE"] = np.full(shape=(subsidy_period,self.ATTR["NUMBER_SCENARIOS"]), fill_value=sales_price)
        elif isinstance(sales_price, list):
            if len(sales_price) == subsidy_period:
                SALES_PRICE_ARRAY = np.array(sales_price)
                SALES_PRICE_ARRAY_2D = SALES_PRICE_ARRAY[:, np.newaxis]*np.ones(self.ATTR["NUMBER_SCENARIOS"])
                self.ATTR["SALES_PRICE"] = SALES_PRICE_ARRAY_2D
            else:
                raise AttributeError("Length of array -sales_price- does not equal funding period.")
        elif isinstance(sales_price, np.ndarray):
            shape_array = sales_price.shape
            dim_array = sales_price.ndim
            upper_limits = sales_price * 1.10
            lower_limits = sales_price * 0.9
            if dim_array == 1:
                if shape_array[0] == subsidy_period:
                    drift = (sales_price[-1] - sales_price[0]) / (subsidy_period - 1)
                    SALES_PRICE_ARRAY_2D = sales_price[:, np.newaxis] * np.ones(self.ATTR["NUMBER_SCENARIOS"])
                    SALES_PRICE_ARRAY_2D[0, :] = sales_price[0]
                    # Apply Geometric Brownian Motion for subsequent periods
                    for t in range(1, subsidy_period):
                        random_shocks = np.random.normal(0, np.sqrt(1),
                                                         self.ATTR["NUMBER_SCENARIOS"])
                        SALES_PRICE_ARRAY_2D[t, :] = SALES_PRICE_ARRAY_2D[t - 1, :] + (drift * 1) + self.ATTR["VOLATILITY"] * random_shocks

                        SALES_PRICE_ARRAY_2D[t, :] = np.where(SALES_PRICE_ARRAY_2D[t, :] > upper_limits[t],
                                                              upper_limits[t], SALES_PRICE_ARRAY_2D[t, :])
                        SALES_PRICE_ARRAY_2D[t, :] = np.where(SALES_PRICE_ARRAY_2D[t, :] < lower_limits[t],
                                                              lower_limits[t], SALES_PRICE_ARRAY_2D[t, :])

                    self.ATTR["SALES_PRICE"] = SALES_PRICE_ARRAY_2D
                else:
                    raise AttributeError("Length of array -sales_price- does not equal funding period.")
            elif dim_array == 2:
                if shape_array[0] == subsidy_period and shape_array[1] == self.ATTR["NUMBER_SCENARIOS"]:
                    self.ATTR["SALES_PRICE"] = sales_price
                else:
                    raise AttributeError("Dimensions of array -sales_price- do not fit definitions for period and simulated scenarios.")
            else:
                raise AttributeError("Dimensions of array -sales_price- must be 1 or 2.")
        else:
            raise AttributeError("Unknown input format for attribute -sales_price-")

        #Keyword arguments
        #____Ratio of reinvested capital from hydrogen sales
        self.ATTR["REINVEST_RATE"] = kwargs.get("REINVEST_RATE", 1)
        #____Number of reinvestment cycles per year
        self.ATTR["REINVEST_CYCLES"] = kwargs.get("REINVEST_CYCLES", 1)
        #____Ratio of sold hydrogen derivatives, relative to purchased hydrogen.
        self.ATTR["SALES_RATE"] = kwargs.get("SALES_RATE", 1)
        #____Subsidy distribution type
        subsidy_distribution = kwargs.get("SUBSIDY_DISTRIBUTION", "constant") #Options: 1 - "constant", 2 - "ramp-up"
        #____Ratio of long- & short-term sales agreements. HSA: Hydrogen sales agreement
        self.ATTR["RATIO_LONGTERM_HSA"] = kwargs.get("RATIO_LONGTERM_HSA", 0)
        self.ATTR["RATIO_SHORTTERM_HSA"] = 1-self.ATTR["RATIO_LONGTERM_HSA"]
        self.ATTR["RATIO_GUARANTEED_SHORTTERM_HSA"] = kwargs.get("RATIO_GUARANTEED_SHORTTERM_HSA", 0)

        #____Define bid-cap and floor-price, if RATIO_LONGTERM_HSA > 0
        if self.ATTR["RATIO_LONGTERM_HSA"] > 0:
            min_sales_price = np.min(self.ATTR["SALES_PRICE"])
            max_sales_price = np.max(self.ATTR["SALES_PRICE"])
            self.ATTR["FLOOR_PRICE_HSA"] = kwargs.get("FLOOR_PRICE_HSA", min_sales_price*0.9)
            self.ATTR["BID_CAP_HSA"] = kwargs.get("BID_CAP_HSA", max_sales_price*0.9)
            self.ATTR["FLOOR_PRICE_HSA_STORE"] = self.ATTR["FLOOR_PRICE_HSA"]
            self.ATTR["BID_CAP_HSA_STORE"] = self.ATTR["BID_CAP_HSA"]

            
        #____Define synthetic floor and cap
        self.ATTR["SYNTHETIC"] = kwargs.get("SYNTHETIC_FLOOR_CAP", False)
        if self.ATTR["SYNTHETIC"]:
            if self.ATTR["RATIO_LONGTERM_HSA"] == 0:
                raise AttributeError("RATIO_LONGTERM_HSA must be >0 to enable SYNTHETIC_FLOOR_CAP")
            else:
                self.ATTR["SYNTH_CAP"] = kwargs.get("SYNTH_CAP", self.ATTR["BID_CAP_HSA"]*1.1)
                self.ATTR["SYNTH_FLOOR"] = kwargs.get("SYNTH_FLOOR", self.ATTR["FLOOR_PRICE_HSA"]*1.1)
                #The premium is an annual cashflow which must be paid to the one lifting the cap or the floor.
                DEFAULT_PREMIUM = self.ATTR["SUBSIDY_VOLUME"]/self.ATTR["SUBSIDY_PERIOD"]*0.05
                self.ATTR["SYNTH_CAP_PREMIUM"] = kwargs.get("SYNTH_CAP_PREMIUM", DEFAULT_PREMIUM)
                self.ATTR["SYNTH_FLOOR_PREMIUM"] = kwargs.get("SYNTH_FLOOR_PREMIUM", DEFAULT_PREMIUM)
        
            self.ATTR["FLOOR_PRICE_HSA"] = self.ATTR["SYNTH_FLOOR"]
            self.ATTR["BID_CAP_HSA"] = self.ATTR["SYNTH_CAP"]
        else:
            self.ATTR["SYNTH_CAP_PREMIUM"] = 0
            self.ATTR["SYNTH_FLOOR_PREMIUM"] = 0

        
        #Initialize output dictionaries (to be calculated)
        #____Purchased quantity of hydrogen derivative per year [kg]
        self.ATTR["Yearly_Product_Purchases"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))       
        #____Purchased quantity of hydrogen derivative per year via long-term contracts [kg]
        self.ATTR["Yearly_Product_Purchases_LONG"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))       
        #____Purchased quantity of hydrogen derivative per year via short-term requests [kg]
        self.ATTR["Yearly_Product_Purchases_SHORT"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))       

        #____Purchased hydrogen derivative per year [$]
        self.ATTR["Yearly_Purchases"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))
        #____Purchased hydrogen derivative per year via long-term offtake agreement [$]
        self.ATTR["Yearly_Purchases_LONG"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))
        #____Purchased hydrogen derivative per year via additional short-term purchases [$]
        self.ATTR["Yearly_Purchases_SHORT"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))
        #____Purchased financial products to decrease volatility
        self.ATTR["Yearly_Purchases_Financial"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))
        #____Sold quantity of hydrogen derivative per year [kg]
        self.ATTR["Yearly_Product_Sales"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))
        #____Sold hydrogen derivative per year [$]
        self.ATTR["Yearly_Sales"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))
        #____Sold hydrogen derivative per year [$]
        self.ATTR["Yearly_Sales_Dict"] = {
            "Sales_to_HSA_LONG" : np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"])),
            "Sales_to_HSA_SHORT" : np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"])),
            } 
        #____Annual requested funding volume per year [$]
        self.ATTR["Yearly_Used_Funding"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))
        
        #____Available capital from reinvested sales per year [$]
        self.ATTR["Yearly_Reinvest_Volume"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))
        self.ATTR["Yearly_Guarantee_Volume"] = np.zeros(shape=(subsidy_period, self.ATTR["NUMBER_SCENARIOS"]))

        #____Available capital from subsidy per year [$]
        if subsidy_distribution == "constant":
            #constant distribution of available capital from subsidy
            self.ATTR["Yearly_Subsidy_Volume"] = np.array([subsidy_volume/subsidy_period for y in range(subsidy_period)])
        elif subsidy_distribution == "ramp-up" and subsidy_period == 10:
            #capital distribution according to lot 1 of H2Global mechanism:
            #ABSOLUTE: year 1: 20 Mio., year 2: 60 Mio., year 3+: 102,5 Mio.
            #RELATIVE: year 1: 2/90, year 2: 6/90 Mio., year 3+: 1025/9000
            self.ATTR["Yearly_Subsidy_Volume"] = []
            for y in range(subsidy_period):
                if y == 0:
                    self.ATTR["Yearly_Subsidy_Volume"].append(subsidy_volume*2/90)
                elif y == 1:
                    self.ATTR["Yearly_Subsidy_Volume"].append(subsidy_volume*6/90)
                else:
                    self.ATTR["Yearly_Subsidy_Volume"].append(subsidy_volume*1025/9000)
            #convert list to numpy array
            Yearly_Subsidy_Volume_List = self.ATTR["Yearly_Subsidy_Volume"].copy()
            self.ATTR["Yearly_Subsidy_Volume"] = np.array(Yearly_Subsidy_Volume_List)
        else:
            raise AttributeError("No such subsidy distribution available or distribution does not match subsidy period.")

    
    def simulate_mechanism(self):
        
        #iterate over years
        for y in range(self.ATTR["SUBSIDY_PERIOD"]):
            
            #get temporary purchase price --> Is a constant value in most cases due to long-term offtake!
            purchase_price_temp = self.ATTR["PURCHASE_PRICE"][y]
            #Get short- & long-term sales price
            sales_price_SHORT_temp = self.ATTR["SALES_PRICE"][y].copy()
                        
            if self.ATTR["RATIO_LONGTERM_HSA"] > 0:
                sales_price_LONG_temp = sales_price_SHORT_temp.copy()
                #adjust for FLOOR_PRICE_HSA
                sales_price_LONG_temp[sales_price_LONG_temp<self.ATTR["FLOOR_PRICE_HSA"]] = self.ATTR["FLOOR_PRICE_HSA"]
                #adjust for BID_CAP_HSA
                sales_price_LONG_temp[sales_price_LONG_temp>self.ATTR["BID_CAP_HSA"]] = self.ATTR["BID_CAP_HSA"]

            #SHORT-TERM HSA
            if self.ATTR["RATIO_SHORTTERM_HSA"] > 0:
                #Initial temporary values for hydrogen purchases from reinvestment 
                RATIO_NO_GUARANTEE = 1-self.ATTR["RATIO_GUARANTEED_SHORTTERM_HSA"]
                RATIO_GUARANTEE = self.ATTR["RATIO_GUARANTEED_SHORTTERM_HSA"]
                
                purchases_reinvest_volume = 0
                SALES_FACTOR_SHORT = self.ATTR["SALES_RATE"]*(sales_price_SHORT_temp/purchase_price_temp)
                REINVEST_FACTOR = self.ATTR["REINVEST_RATE"]
                if self.ATTR["REINVEST_CYCLES"] > 0:
                    for c in range(self.ATTR["REINVEST_CYCLES"]):
                        if c==0:
                            #get purchases of cycle before! - First cycle is sales from base funding
                            purchases_base_subsidy = self.ATTR["Yearly_Subsidy_Volume"][y]*self.ATTR["RATIO_SHORTTERM_HSA"]*RATIO_NO_GUARANTEE
                            #get sales from previous cycle
                            sales_cycle = purchases_base_subsidy*SALES_FACTOR_SHORT
                            purchases_reinvest_volume += sales_cycle
                        else:
                            #get sales from previous cycle
                            sales_cycle = sales_cycle*SALES_FACTOR_SHORT*REINVEST_FACTOR
                            purchases_reinvest_volume += sales_cycle
                elif self.ATTR["REINVEST_CYCLES"] == -1:
                    #Calculate the INITIAL purchases for secured long-term sales agreements --> Purchases = Funding.
                    purchases_base_subsidy_SHORT = self.ATTR["Yearly_Subsidy_Volume"][y]*self.ATTR["RATIO_SHORTTERM_HSA"]*RATIO_NO_GUARANTEE
                    price_delta_SHORT = purchase_price_temp-sales_price_SHORT_temp
                    #purchases_base_subsidy_SHORT_TOTAL are the total purchases, if all sales are certain and only the price delta needs to be funded!
                    purchases_base_subsidy_SHORT_TOTAL = purchases_base_subsidy_SHORT*(purchase_price_temp / price_delta_SHORT)
                    
                    purchases_reinvest_volume = purchases_base_subsidy_SHORT_TOTAL - purchases_base_subsidy_SHORT
                else:
                    print("Assume REINVEST_CYCLES == 0")

                if RATIO_GUARANTEE > 0:
                    #Calculate the INITIAL purchases for secured long-term sales agreements --> Purchases = Funding.
                    purchases_base_subsidy_SHORT = self.ATTR["Yearly_Subsidy_Volume"][y]*self.ATTR["RATIO_SHORTTERM_HSA"]*RATIO_GUARANTEE
                    price_delta_SHORT = purchase_price_temp-sales_price_SHORT_temp
                    purchases_guarantee = purchases_base_subsidy_SHORT*(purchase_price_temp / price_delta_SHORT)
                    self.ATTR["Yearly_Guarantee_Volume"][y] = purchases_guarantee
                else:
                    purchases_guarantee = 0
                    self.ATTR["Yearly_Guarantee_Volume"][y] = 0
                    
                #update calculation of purchases and sales after reinvestment
                self.ATTR["Yearly_Reinvest_Volume"][y] = purchases_reinvest_volume
                
                #additional short-term purchases from additional sales revenue
                purchases_in_dollar_SHORT_temp = (
                    self.ATTR["Yearly_Reinvest_Volume"][y]
                    )
                #Purchases from long-term purchase agreements (10y offtake contract)
                purchases_in_dollar_LONG_temp = (
                    self.ATTR["Yearly_Subsidy_Volume"][y]*self.ATTR["RATIO_SHORTTERM_HSA"]*RATIO_NO_GUARANTEE + purchases_guarantee
                    )
                
                sales_in_dollar_SHORT_temp = (purchases_in_dollar_SHORT_temp+purchases_in_dollar_LONG_temp)*SALES_FACTOR_SHORT
                self.ATTR["Yearly_Sales_Dict"]["Sales_to_HSA_SHORT"][y] += sales_in_dollar_SHORT_temp
                
            #LONG-TERM HSA
            if self.ATTR["RATIO_LONGTERM_HSA"] > 0:
                #Calculate the INITIAL purchases for secured long-term sales agreements
                annual_premium_payments = self.ATTR["SYNTH_CAP_PREMIUM"] + self.ATTR["SYNTH_FLOOR_PREMIUM"]
                base_subsidy_LONG = self.ATTR["Yearly_Subsidy_Volume"][y]*self.ATTR["RATIO_LONGTERM_HSA"]-annual_premium_payments
                price_delta_LONG = purchase_price_temp-self.ATTR["FLOOR_PRICE_HSA"]
                purchases_base_subsidy_LONG = base_subsidy_LONG*(purchase_price_temp / price_delta_LONG)
                sales_in_dollar_base_subsidy_LONG = purchases_base_subsidy_LONG * (sales_price_LONG_temp / purchase_price_temp)
                
                #Purchases and sales for long-term conditions
                if self.ATTR["RATIO_SHORTTERM_HSA"] > 0:
                    purchases_in_dollar_LONG_temp += purchases_base_subsidy_LONG
                else:
                    purchases_in_dollar_LONG_temp = purchases_base_subsidy_LONG
                sales_in_dollar_LONG_temp = sales_in_dollar_base_subsidy_LONG
                
                self.ATTR["Yearly_Sales_Dict"]["Sales_to_HSA_LONG"][y] += sales_in_dollar_LONG_temp
                
                #Calculate the ADDITIONAL purchases, if market price > floor-price
                additional_CAPITAL_SHORT = purchases_base_subsidy_LONG * (
                    (sales_price_LONG_temp - self.ATTR["FLOOR_PRICE_HSA"]) / purchase_price_temp
                    )
                
                #PROCESS FOR PURCHASING SHORT WITH ADDITIONAL CAPITAL
                purchases_reinvest_volume_LONG = 0
                SALES_FACTOR_SHORT = self.ATTR["SALES_RATE"]*(sales_price_SHORT_temp/purchase_price_temp)
                REINVEST_FACTOR = self.ATTR["REINVEST_RATE"]                
                if self.ATTR["REINVEST_CYCLES"] > 0:
                    for c in range(self.ATTR["REINVEST_CYCLES"]):
                        if c==0:
                            #get sales from previous cycle
                            sales_cycle = additional_CAPITAL_SHORT*SALES_FACTOR_SHORT
                            purchases_reinvest_volume_LONG += sales_cycle
                        else:
                            #get sales from previous cycle
                            sales_cycle = sales_cycle*SALES_FACTOR_SHORT*REINVEST_FACTOR
                            purchases_reinvest_volume_LONG += sales_cycle
                elif self.ATTR["REINVEST_CYCLES"] == -1:
                    #Calculate the INITIAL purchases for secured long-term sales agreements --> Purchases = Funding.
                    price_delta_SHORT = purchase_price_temp-sales_price_SHORT_temp
                    #purchases_base_subsidy_SHORT_TOTAL are the total purchases, if all sales are certain and only the price delta needs to be funded!
                    purchases_base_subsidy_SHORT_TOTAL = additional_CAPITAL_SHORT*(purchase_price_temp / price_delta_SHORT)
                    
                    purchases_reinvest_volume_LONG = purchases_base_subsidy_SHORT_TOTAL - additional_CAPITAL_SHORT
                else:
                    print("Assume REINVEST_CYCLES == 0")

                purchases_additional_SHORT = additional_CAPITAL_SHORT + purchases_reinvest_volume_LONG
                
                #____Account for the case that market price < floor-price!
                purchases_additional_SHORT[purchases_additional_SHORT<0] = 0
                #____Derive sales from the purchases.
                sales_in_dollar_additional_SHORT = purchases_additional_SHORT * (sales_price_SHORT_temp / purchase_price_temp)
                
                #Additional short-term purchases and sales due to above-floor prices.
                if self.ATTR["RATIO_SHORTTERM_HSA"] > 0:
                    purchases_in_dollar_SHORT_temp += purchases_additional_SHORT
                    sales_in_dollar_SHORT_temp += sales_in_dollar_additional_SHORT
                else:
                    purchases_in_dollar_SHORT_temp = purchases_additional_SHORT
                    sales_in_dollar_SHORT_temp = sales_in_dollar_additional_SHORT
                self.ATTR["Yearly_Sales_Dict"]["Sales_to_HSA_SHORT"][y] += sales_in_dollar_additional_SHORT
                
            #FINAL CALCULATION OF PURCHASES AND SALES
            if self.ATTR["RATIO_LONGTERM_HSA"] > 0:

                purchases_in_dollar_TOTAL_temp = purchases_in_dollar_SHORT_temp + purchases_in_dollar_LONG_temp
                sales_in_dollar_TOTAL_temp = sales_in_dollar_SHORT_temp + sales_in_dollar_LONG_temp
                #Calculate sold quantity of hydrogen derivative per year [kg]
                self.ATTR["Yearly_Product_Sales"][y] = (
                    sales_in_dollar_SHORT_temp / sales_price_SHORT_temp + 
                    sales_in_dollar_LONG_temp / sales_price_LONG_temp
                    )
            else:
                purchases_in_dollar_TOTAL_temp = purchases_in_dollar_SHORT_temp + purchases_in_dollar_LONG_temp
                sales_in_dollar_TOTAL_temp = sales_in_dollar_SHORT_temp
                #Calculate sold quantity of hydrogen derivative per year [kg]
                self.ATTR["Yearly_Product_Sales"][y] = sales_in_dollar_SHORT_temp / sales_price_SHORT_temp

            #Calculate purchased quantity of hydrogen derivative per year [kg]
            self.ATTR["Yearly_Product_Purchases"][y] = purchases_in_dollar_TOTAL_temp / purchase_price_temp
            self.ATTR["Yearly_Product_Purchases_LONG"][y] = purchases_in_dollar_LONG_temp / purchase_price_temp
            self.ATTR["Yearly_Product_Purchases_SHORT"][y] = purchases_in_dollar_SHORT_temp / purchase_price_temp
                        
            #Assign annual sales
            self.ATTR["Yearly_Sales"][y] = sales_in_dollar_TOTAL_temp
            #Assign annual purchases
            self.ATTR["Yearly_Purchases"][y] = purchases_in_dollar_TOTAL_temp
            self.ATTR["Yearly_Purchases_LONG"][y] = purchases_in_dollar_LONG_temp
            self.ATTR["Yearly_Purchases_SHORT"][y] = purchases_in_dollar_SHORT_temp
            #Calculate financial purchases
            if self.ATTR["SYNTHETIC"]:
                self.ATTR["Yearly_Purchases_Financial"][y] = self.ATTR["SYNTH_CAP_PREMIUM"] + self.ATTR["SYNTH_FLOOR_PREMIUM"]
            else:
                self.ATTR["Yearly_Purchases_Financial"][y] = 0
            #Utilized funding volume
            funding_request = purchases_in_dollar_TOTAL_temp + self.ATTR["Yearly_Purchases_Financial"][y] - sales_in_dollar_TOTAL_temp
            if min(funding_request) < 0:
                print("Funding request <0 in year", y)
                funding_request = 0
            self.ATTR["Yearly_Used_Funding"][y] = funding_request
            