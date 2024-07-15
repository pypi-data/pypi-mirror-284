
import itertools
import json
from datetime import datetime

import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

from minitrade.broker.base import BrokerAccount
from minitrade.datasource import QuoteSource
from minitrade.datasource.union import UnionQuoteSource, UnionQuoteSourceConfig
from minitrade.utils.config import config

st.set_page_config(page_title='Datasource', layout='wide')


def test_and_save_yahoo_proxy(proxy):
    st.caption('Getting SPY')
    df = QuoteSource.get_source('Yahoo', proxy=proxy).daily_bar('SPY', start='2023-01-01')
    if len(df) > 0:
        st.write(df)
        config.sources.yahoo.proxy = proxy
        config.save()
        st.success('Setting saved')
    else:
        st.error('Getting data from Yahoo not working, please check proxy setting')


def test_and_save_eodhd_api_key(api_key):
    st.caption('Getting SPY')
    df = QuoteSource.get_source('EODHistoricalData', api_key=api_key).daily_bar('SPY', start='2023-01-01')
    if len(df) > 0:
        st.write(df)
        config.sources.eodhd.api_key = api_key
        config.save()
        st.success('Setting saved')
    else:
        st.error('Getting data from EODHistoricalData not working, please check API key')


def test_and_save_twelvedata_api_key(api_key):
    st.caption('Getting SPY')
    df = QuoteSource.get_source('TwelveData', api_key=api_key).daily_bar('SPY', start='2023-01-01')
    if len(df) > 0:
        st.write(df)
        config.sources.twelvedata.api_key = api_key
        config.save()
        st.success('Setting saved')
    else:
        st.error('Getting data from TwelveData not working, please check API key')


def test_and_save_alpaca_api_key(api_key, api_secret):
    st.caption('Getting SPY')
    df = QuoteSource.get_source('Alpaca', api_key=api_key, api_secret=api_secret).daily_bar('SPY', start='2023-01-01')
    if len(df) > 0:
        st.write(df)
        config.sources.alpaca.api_key = api_key
        config.sources.alpaca.api_secret = api_secret
        config.save()
        st.success('Setting saved')
    else:
        st.error('Getting data from Alpaca not working, please check API key')


def test_and_save_tiingo_api_key(api_key):
    st.caption('Getting SPY')
    df = QuoteSource.get_source('Tiingo', api_key=api_key).daily_bar('SPY', start='2023-01-01')
    if len(df) > 0:
        st.write(df)
        config.sources.tiingo.api_key = api_key
        config.save()
        st.success('Setting saved')
    else:
        st.error('Getting data from Tiingo not working, please check API key')


def test_and_save_ib_account(alias):
    st.caption('Getting SPY')
    df = QuoteSource.get_source('InteractiveBrokers', alias=alias).daily_bar('SPY', start='2023-01-01')
    if len(df) > 0:
        st.write(df)
        config.sources.ib.account = alias
        config.save()
        st.success('Setting saved')
    else:
        st.error('Getting data from InteractiveBrokers not working, please check account')


def confirm_delete_union_data_source(source) -> None:
    def confirm_delete():
        if st.session_state.delete_confirm_textinput == source:
            UnionQuoteSourceConfig.get_config(source).delete()
    st.text_input(f'Type "{source}" and press Enter to delete',
                  on_change=confirm_delete, key='delete_confirm_textinput')


def show_source_page():
    source = st.sidebar.radio('Source', QuoteSource.list())

    c1, c2 = st.columns([5, 1], gap='large')
    c1.subheader(source)
    if source in QuoteSource.list():
        if c2.button('Delete', type='primary'):
            confirm_delete_union_data_source(source)
    t1, t2 = st.tabs(['Config', 'About'])
    with t1:
        config_source(source)
    with t2:
        about_source(source)


def about_source(source):
    if source in QuoteSource.list():
        st.markdown(QuoteSource.get_source(source).__doc__ or '')
    else:
        st.write('Unknown data source')


def config_source(source):
    if source == 'Yahoo':
        proxy = st.text_input('HTTP Proxy (Socks proxy not supported)',
                              placeholder='http://host:port', value=config.sources.yahoo.proxy or '') or None
        if st.button('Test and save'):
            test_and_save_yahoo_proxy(proxy)
    elif source == 'EastMoney':
        st.write('Nothing to configure')
    elif source == 'EODHistoricalData':
        api_key = st.text_input('API Key', value=config.sources.eodhd.api_key or '') or None
        if st.button('Test and save'):
            test_and_save_eodhd_api_key(api_key)
    elif source == 'TwelveData':
        api_key = st.text_input('API Key', value=config.sources.twelvedata.api_key or '') or None
        if st.button('Test and save'):
            test_and_save_twelvedata_api_key(api_key)
    elif source == 'Alpaca':
        api_key = st.text_input('API Key', value=config.sources.alpaca.api_key or '') or None
        api_secret = st.text_input('API Secret', value=config.sources.alpaca.api_secret or '') or None
        if st.button('Test and save'):
            test_and_save_alpaca_api_key(api_key, api_secret)
    elif source == 'Tiingo':
        api_key = st.text_input('API Key', value=config.sources.tiingo.api_key or '') or None
        if st.button('Test and save'):
            test_and_save_tiingo_api_key(api_key)
    elif source == 'InteractiveBrokers':
        accounts = [_ for _ in BrokerAccount.list() if _.broker == 'IB']
        if len(accounts) == 0:
            st.warning('Please make sure you have configured your IB account in the broker section.')
            return
        alias = st.selectbox('Use for data access', [_.alias for _ in accounts])
        if st.button('Save'):
            config.sources.ib.account = alias
            config.save()
            st.success('Setting saved')
        if config.sources.ib.account:
            st.success(f'Currently using account "**{config.sources.ib.account}**" for data access.')
        else:
            st.error('No account is currently configured for data access.')
    elif source == 'CboeIndex':
        st.write('Nothing to configure')
    elif source == 'CboeFutures':
        st.write('Nothing to configure')
    elif source in UnionQuoteSource.list():
        st.write('This is an union data source configured as follows:')
        union_config = UnionQuoteSourceConfig.get_config(source).config
        for ticker, name, params in union_config:
            st.caption(ticker or 'Catch-all')
            if params:
                params = ', '.join([f'{k}={v}' for k, v in params.items()])
                st.code(f'QuoteSource.get_source("{name}", {params})')
            else:
                st.code(f'QuoteSource.get_source("{name}")')
    else:
        st.write('Unknown data source')


@st.cache_data(ttl='1h')
def read_daily_bar(ticker, start, end, sources):
    data = {}
    for s in sources:
        try:
            data[s] = QuoteSource.get_source(s).daily_bar(ticker, start=start, end=end)
        except Exception as e:
            raise RuntimeError(f'Getting {s} data error: {e}')
    return data


def compare_data_from_sources(data, s1, s2, tab):
    df1 = data[s1].droplevel(0, axis=1)
    df2 = data[s2].droplevel(0, axis=1)
    df = pd.merge(df1, df2, how='outer', left_index=True, right_index=True, suffixes=('_1', '_2'))
    cols = tab.columns(5)
    for col, c in zip(cols, ['Open', 'High', 'Low', 'Close', 'Volume']):
        col.write(c)
        res = calc_col_diff(s1, s2, df, c)
        col.dataframe(res)
        # plot s1 vs s2
        fig = plot_price(s1, s2, c, res)
        col.pyplot(fig)
        plt.close(fig)
        # print diff stats
        col.write('Diff stats')
        stats = res['diff (%)'].describe()[['count', 'mean', 'std', 'min', 'max']].to_frame().T
        col.write(stats)
        # print top 3 diff
        col.write('Top 3 diff')
        col.write(res.sort_values('diff (%)', ascending=False, key=abs).head(3))
        # plot diff
        fig = plot_diff(c, res)
        col.pyplot(fig)
        plt.close(fig)


def plot_diff(c, res):
    fig, ax = plt.subplots()
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.set_xticks([])
    ax.plot(res.index, res['diff (%)'])
    ax.set_title(f'{c} diff (%)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Diff (%)')
    fig.set_size_inches(6, 3)
    return fig


def plot_price(s1, s2, c, res):
    fig, ax = plt.subplots()
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.set_xticks([])
    ax.plot(res.index, res[s1], label=s1)
    ax.plot(res.index, res[s2], label=s2)
    ax.legend()
    ax.set_title(f'{c} {s1} vs {s2}')
    ax.set_xlabel('Date')
    ax.set_ylabel(c)
    fig.set_size_inches(6, 3)
    return fig


@st.cache_data(ttl='1h')
def calc_col_diff(s1, s2, df, c):
    df[f'{c} diff'] = df[f'{c}_2'] - df[f'{c}_1']
    df[f'{c} diff (%)'] = df[f'{c} diff'] / df[f'{c}_1'] * 100
    res = df[[f'{c}_1', f'{c}_2', f'{c} diff', f'{c} diff (%)']]
    res.columns = [s1, s2, 'diff', 'diff (%)']
    res.index = res.index.strftime('%Y-%m-%d')
    return res


def plot_ohlcv(data):
    for ticker in data.columns.get_level_values(0).unique():
        c1, c2, c3 = st.columns(3)
        df = data[ticker]
        # print ohlcv
        c1.write(f'### {ticker}')
        c1.dataframe(df)
        c1.download_button(f'Download {ticker}', df.to_csv().encode('utf-8'), f'{ticker}.csv')
        # plot stats
        c2.write('### Stats')
        stats = df.describe()
        c2.dataframe(stats)
        # plot ohlcv
        fig, ax = plt.subplots()
        ax.xaxis.set_tick_params(labelbottom=False)
        ax.set_xticks([])
        ax.plot(df.index, df['Open'], label='Open')
        ax.plot(df.index, df['High'], label='High')
        ax.plot(df.index, df['Low'], label='Low')
        ax.plot(df.index, df['Close'], label='Close')
        ax.legend()
        ax.set_title(f'{ticker}')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        # plot volume
        ax2 = ax.twinx()
        ax2.bar(df.index, df['Volume'], label='Volume', alpha=0.3)
        ax2.set_ylabel('Volume')
        ax2.legend(loc='upper right')
        ax2.grid(False)
        fig.set_size_inches(8, 4)
        c3.write('### Chart')
        c3.pyplot(fig)
        plt.close(fig)
        st.write('---')


def inspect_data():
    tickers = st.sidebar.text_input('Ticker', value='SPY')
    start = st.sidebar.text_input('Start date', value='2000-01-01') or None
    end = st.sidebar.text_input('End date') or None
    sources = st.sidebar.multiselect('Sources', QuoteSource.list(), default=['Yahoo'])

    if len(sources) == 1 and st.sidebar.button('Inspect'):
        if len(sources) == 1:
            st.write(f'## {sources[0]}')
            try:
                df = read_daily_bar(tickers, start, end, sources)[sources[0]]
                plot_ohlcv(df)
            except Exception as e:
                st.error(e)
    if len(sources) > 1 and st.sidebar.button('Compare'):
        if len(tickers.split(',')) > 1:
            st.sidebar.warning('Only the first ticker will be compared.')
        tickers = tickers.split(',')[0]
        st.write(f'## {tickers}')
        data = read_daily_bar(tickers, start, end, sources)
        pairs = list(itertools.combinations(sources, 2))
        tabs = st.tabs([(f'{s1} vs {s2}') for s1, s2 in pairs])
        for i, (s1, s2) in enumerate(pairs):
            with tabs[i]:
                compare_data_from_sources(data, s1, s2, tabs[i])


def lookup_ticker():
    if not config.sources.ib.account:
        st.sidebar.warning('Please make sure you have configured the IB account for data access.')
        return
    source = QuoteSource.get_source('InteractiveBrokers')
    tickers = st.sidebar.text_input('Lookup IB contract ID', placeholder='SPY,QQQ')
    if st.sidebar.button('Lookup'):
        idmap = source.lookup(tickers)
        st.header('Result')
        for k, idlst in idmap.items():
            with st.expander(k, expanded=True):
                if len(idlst) == 0:
                    st.write('No found')
                else:
                    for item in idlst:
                        st.write(f'{item["id"]} - {item["label"]}')


def create_union_source():
    st.subheader('Create union data source')
    st.info('A union data source let you retrieve data for different tickers using different data sources. '
            'You can explicitly map tickers to data sources. '
            'You can also define a catch-all data source for tickers not found in the mapping.')

    source_name = st.text_input('Data source name')
    with st.expander('Sources', expanded=True):
        tabs = st.tabs('12345678')
        ticker = [None] * 8
        name = [None] * 8
        params = [None] * 8
        for i, tab in enumerate(tabs):
            with tab:
                ticker[i] = st.text_input('Tickers (comma separated list without space)', key=f'ticker_{i}')
                name[i] = st.selectbox('Source', QuoteSource.SYSTEM_SOURCES, key=f'name_{i}')
                params[i] = st.text_input(
                    'Params (parameters to be passed to `QuoteSource.get_source()` in JSON format)', key=f'params_{i}',
                    placeholder='{}') or None
                try:
                    if params[i]:
                        params[i] = json.loads(params[i])
                except Exception as e:
                    st.error(f'Invalid JSON: {e}')
    with st.expander('Catch-all source', expanded=True):
        catchall = st.selectbox('Source', [None] + QuoteSource.SYSTEM_SOURCES)
        catchall_params = st.text_input('Params') or None
        try:
            if catchall_params:
                json.loads(catchall_params)
        except Exception as e:
            st.error(f'Invalid JSON: {e}')
    save = st.button('Save')
    if save:
        if not source_name:
            st.error('Data source name is required')
            return
        elif source_name in QuoteSource.SYSTEM_SOURCES:
            st.error(f'"{source_name}" is a built-in data source')
            return
        union_config = [(t, n, p) for t, n, p in zip(ticker, name, params) if t and n]
        if catchall:
            union_config.append((None, catchall, catchall_params))
        UnionQuoteSource(union_config)    # test if the config is valid
        union = UnionQuoteSourceConfig(
            name=source_name,
            config=union_config,
            update_time=datetime.utcnow()
        )
        union.save()
        st.success(f'Union data source "{source_name}" saved')


action = st.sidebar.radio('Action', ['Config', 'Create', 'Inspect', 'Lookup (IB only)'])

if action == 'Config':
    show_source_page()


if action == 'Create':
    create_union_source()


if action == 'Inspect':
    inspect_data()


if action == 'Lookup (IB only)':
    lookup_ticker()
