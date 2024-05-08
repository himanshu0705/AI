import streamlit as st

knowledge_base = {
    "Risk Tolerance": [
        "1: Conservative - Low-risk investments like bonds or savings accounts.",
        "2: Moderate - Balanced portfolio with a mix of stocks and bonds.",
        "3: Aggressive - High-risk investments like stocks or cryptocurrencies."
    ],

    "Investment Goals": [
        "1: Retirement planning - Consider long-term investments with compounding interest.",
        "2: Wealth accumulation - Focus on growth-oriented investments.",
        "3: Education funding - Explore options like 529 plans or education savings accounts."
    ],

    "Investment Strategies": [
        "1: Dollar-cost averaging - Regularly invest a fixed amount regardless of market fluctuations.",
        "2: Diversification - Spread investments across different asset classes to reduce risk.",
        "3: Value investing - Seek undervalued assets for long-term growth potential."
    ],

    "Investment Options": [
        "1: Stocks - Ownership in a company, potential for high returns but also higher risk.",
        "2: Bonds - Fixed-income securities with lower risk and returns compared to stocks.",
        "3: Mutual Funds - Pooled funds managed by professionals, offering diversification.",
        "4: Real Estate - Investment in properties for rental income or capital appreciation.",
        "5: ETFs (Exchange-Traded Funds) - Funds traded on stock exchanges, offering diversification.",
        "6: Cryptocurrencies - Digital assets with high volatility, suitable for speculative investors."
    ],

    "Risk Factors": [
        "1: Market Risk - Fluctuations in the market affecting the value of investments.",
        "2: Inflation Risk - Decrease in purchasing power over time due to rising prices.",
        "3: Interest Rate Risk - Changes in interest rates affecting bond prices.",
        "4: Liquidity Risk - Difficulty in selling assets without significant loss.",
        "5: Currency Risk - Fluctuations in exchange rates affecting international investments."
    ],

    "Tax Efficiency": [
        "1: Tax-Advantaged Accounts - IRAs, 401(k)s, offering tax benefits for retirement savings.",
        "2: Capital Gains Tax Planning - Strategies to minimize taxes on investment gains.",
        "3: Tax-Loss Harvesting - Offsetting capital gains with capital losses for tax purposes."
    ]
}

def respond(input :str):
    if input in knowledge_base:
        for value in knowledge_base[input]:
            st.write(value)
    else:
        st.write("Sorry! the system couldn't find the suitable response for your query")

if __name__ == "__main__":
    options = st.selectbox(
        "What aspects of investment are you interested in?",
        ["Risk Tolerance","Investment Goals","Investment Strategies","Investment Options","Risk Factors","Tax Efficiency"]
    )
    col1,col2 = st.columns([1,0.1])
    with col1:
        ask = st.button("Ask")
    with col2:
        quit = st.button("Quit")
    if (ask):
        respond(options)
    if(quit):
        st.write("Thankyou for using Investment Advisory Expert System")