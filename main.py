import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz
import math
import importlib
import numpy as np  # NaN 처리를 위해 추가

# ---------------------------------------------------------
# [설정] 앱 기본 설정
# ---------------------------------------------------------
st.set_page_config(
    page_title="배당금 통합 계산기",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# [데이터 로드]
# ---------------------------------------------------------
MODULE_LIST = [
    ("data_roundhill", "Roundhill", "🌿"),
    ("data_rex", "REX Shares", "🦖"),
    ("data_yieldmax_1", "YieldMax G1", "🚀"),
    ("data_yieldmax_2", "YieldMax G2", "🌌"),
    ("data_granite", "Granite", "💎"),
]

loaded_providers = {}

for module_name, display_name, emoji in MODULE_LIST:
    try:
        mod = importlib.import_module(module_name)
        importlib.reload(mod)
        raw_data = mod.get_data()

        ex_date = raw_data['schedule'].get('ex_date', '미정')
        short_date = ex_date.split('(')[0] if '(' in ex_date else ex_date

        label = f"{emoji} {display_name} ({short_date})"
        loaded_providers[label] = raw_data
    except ImportError:
        continue

if not loaded_providers:
    st.error("❌ 데이터 파일(*.py)을 찾을 수 없습니다.")
    st.stop()

# ---------------------------------------------------------
# [UI - 상단] 운용사 선택
# ---------------------------------------------------------
if 'selected_provider' not in st.session_state:
    st.session_state.selected_provider = list(loaded_providers.keys())[0]

current_selection = st.session_state.get('selected_provider_radio', list(loaded_providers.keys())[0])
data_source = loaded_providers[current_selection]
DATA_MAP = data_source.get('tickers', {})
SCHEDULE_KST = data_source.get('schedule', {})
THEME_COLORS = data_source.get('theme_color', ["#333", "#555"])

# ---------------------------------------------------------
# [함수] HTML/CSS
# ---------------------------------------------------------
def render_html(raw_html):
    cleaned = " ".join([line.strip() for line in raw_html.splitlines() if line.strip()])
    st.markdown(cleaned, unsafe_allow_html=True)

render_html(f"""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

    html, body, [class*="css"] {{
        font-family: 'Pretendard', sans-serif;
        background-color: #f4f6f8 !important;
        color: #191f28 !important;
    }}

    .block-container {{ padding-top: 3.5rem !important; padding-bottom: 5rem !important; }}

    /* 탭 메뉴 스타일 */
    div[data-testid="stRadio"] > div[role="radiogroup"] {{
        display: flex !important; flex-direction: row !important; overflow-x: auto !important; 
        gap: 8px !important; padding: 4px 4px 16px 4px; -webkit-overflow-scrolling: touch; flex-wrap: nowrap !important;
    }}
    div[data-testid="stRadio"] > div[role="radiogroup"]::-webkit-scrollbar {{ display: none; }}

    div[data-testid="stRadio"] label {{
        background: #fff !important; 
        border: 1px solid #e5e8eb !important; 
        border-radius: 20px !important; 
        padding: 8px 14px !important; 
        min-width: max-content; 
        font-size: 0.85rem !important; 
        font-weight: 600 !important;
        color: #6b7684; 
        transition: all 0.2s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }}

    div[data-testid="stRadio"] label:has(input:checked) {{
        background: linear-gradient(135deg, {THEME_COLORS[0]} 0%, {THEME_COLORS[1]} 100%) !important;
        border: 1px solid {THEME_COLORS[0]} !important; 
        color: white !important; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.2); 
        transform: translateY(-2px);
    }}
    div[data-testid="stRadio"] label:has(input:checked) * {{ color: white !important; }}

    /* 핫픽 배너 */
    .hot-banner {{
        background: #fff; border-radius: 16px; padding: 14px 16px; margin-bottom: 16px;
        display: flex !important; flex-direction: row !important; align-items: center !important;
        justify-content: space-between !important; border: 1px solid #eee;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03); white-space: nowrap !important;
    }}

    /* 헤더 카드 */
    .header-card {{
        background: linear-gradient(135deg, {THEME_COLORS[0]} 0%, {THEME_COLORS[1]} 100%);
        padding: 24px 20px; border-radius: 24px; color: white !important;
        margin-bottom: 16px; box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        position: relative; overflow: hidden;
    }}
    .header-card h2, .header-card div, .header-card span {{ color: white !important; }}

    /* 계산 기준 박스 디자인 */
    .caution-box {{
        margin-top: 16px; 
        padding: 16px 20px; 
        background: #fff !important; 
        border-radius: 16px; 
        border: 1px solid #e5e8eb;
        font-size: 0.85rem; 
        color: #555 !important; 
        line-height: 1.6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }}
    .caution-header {{ 
        font-weight: 800; 
        color: #d9534f !important; 
        margin-bottom: 8px; 
        display: block; 
        font-size: 0.95rem;
    }}

    /* 기타 UI */
    .notice-box {{
        background-color: #fff8e1; color: #d97706; padding: 12px 16px; 
        border-radius: 12px; font-size: 0.8rem; margin-bottom: 20px;
        display: flex; align-items: center; gap: 10px; border: 1px solid #ffe0b2;
        box-shadow: 0 2px 4px rgba(217, 119, 6, 0.1); line-height: 1.4;
    }}
    .info-card {{ background: white !important; border-radius: 24px; padding: 24px 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.04); margin-bottom: 20px; border:1px solid #fff; }}
    .grade-badge {{ font-size: 0.75rem; font-weight: 800; padding: 4px 8px; border-radius: 6px; margin-left: 6px; vertical-align: middle; }}
    .calc-card-bg {{ background: #fff !important; border-radius: 20px; padding: 20px; border: 1px solid #edf2f7; margin-top: 10px; }}
    .provider-title {{ font-size: 1.1rem; font-weight: 800; color: #333; margin: 0 0 10px 4px; }}
    div.stButton > button {{ width: 100%; border-radius: 14px; height: 50px; font-weight: 700; background: #fff; border: 1px solid #ddd; }}
    div.stButton > button:hover {{ border-color: {THEME_COLORS[0]}; color: {THEME_COLORS[0]}; }}

    /* 계산기 내부 텍스트 */
    .calc-row {{ display: flex; justify-content: space-between; margin-bottom: 10px; align-items: center; }}
    .calc-label {{ font-size: 0.9rem; color: #666; }}
    .calc-val {{ font-weight: 700; color: #333; }}
    .calc-divider {{ border-top: 1px dashed #e0e0e0; margin: 12px 0; }}
    .calc-total-label {{ font-size: 1rem; font-weight: 700; color: {THEME_COLORS[0]}; }}
    .calc-total-val {{ font-size: 1.4rem; font-weight: 800; color: {THEME_COLORS[0]}; }}
    </style>
""")

# ---------------------------------------------------------
# [데이터 처리 함수] - NaN 에러 방지 강화
# ---------------------------------------------------------
def get_us_market_status():
    ny_tz = pytz.timezone('America/New_York')
    now_ny = datetime.now(ny_tz)
    minutes = now_ny.hour * 60 + now_ny.minute

    if now_ny.weekday() >= 5: return "⛔ 주말 휴장"
    holidays = ["2025-12-25", "2026-01-01", "2026-01-19"]
    if now_ny.strftime("%Y-%m-%d") in holidays: return "⛔ 공휴일 휴장"

    if 570 <= minutes < 960: return "🔥 정규장 (실시간)"
    elif 240 <= minutes < 570: return "🌅 프리마켓"
    elif 960 <= minutes < 1200: return "🌙 애프터마켓"
    else: return "💤 장 마감"

@st.cache_data(ttl=30, show_spinner=False)
def get_market_info(ticker_keys):
    try:
        # 환율 정보
        fx_data = yf.Ticker("USDKRW=X").history(period="1d")["Close"]
        if not fx_data.empty:
            fx = float(fx_data.iloc[-1])
        else:
            fx = 1445.0
    except:
        fx = 1445.0

    prices = {}
    if not ticker_keys: return fx, prices, ""

    try:
        t_str = " ".join(ticker_keys)
        # progress=False로 콘솔 출력 방지
        data = yf.download(t_str, period="1d", progress=False)['Close']

        for t in ticker_keys:
            try:
                # 1개일 때(Series)와 여러 개일 때(DataFrame) 처리
                if len(ticker_keys) == 1:
                    val = data.iloc[-1]
                else:
                    val = data[t].iloc[-1]

                # [핵심] NaN 값 체크 및 0.0 처리
                if pd.isna(val) or np.isnan(val):
                    prices[t] = 0.0
                else:
                    prices[t] = float(val)
            except:
                prices[t] = 0.0
    except:
        pass

    now_time = datetime.now(pytz.timezone('Asia/Seoul')).strftime("%H:%M:%S")
    return fx, prices, now_time

# ---------------------------------------------------------
# [UI 1] 운용사 선택
# ---------------------------------------------------------
st.markdown('<div class="provider-title">💰 운용사 선택</div>', unsafe_allow_html=True)

selected_label = st.radio(
    "운용사 선택",
    list(loaded_providers.keys()),
    index=0,
    horizontal=True,
    key="selected_provider_radio",
    label_visibility="collapsed"
)

data_source = loaded_providers[selected_label]
DATA_MAP = data_source.get('tickers', {})
SCHEDULE_KST = data_source.get('schedule', {})

# ---------------------------------------------------------
# [UI 2] 초보자 TIP
# ---------------------------------------------------------
render_html("""
    <div class="notice-box">
        <span class="tip-icon">🐤</span>
        <div>
            <b>초보자 TIP</b><br>
            버튼 속 날짜는 <b>'배당락일'</b>입니다.<br>
            안전하게 받으려면 <b>전날까지 매수</b>하세요!
        </div>
    </div>
""")

# ---------------------------------------------------------
# [UI 3] 데이터 수신 및 헤더
# ---------------------------------------------------------
if st.button("🔄 실시간 시세 업데이트"):
    st.cache_data.clear()

t_list = sorted(list(DATA_MAP.keys()))
tax_rate = 0.154

with st.spinner("데이터 동기화 중..."):
    usd_krw, price_map, update_time = get_market_info(t_list)
    market_text = get_us_market_status()

if DATA_MAP:
    best_ticker = max(DATA_MAP, key=lambda k: DATA_MAP[k]['rate'])
    best_rate = DATA_MAP[best_ticker]['rate']
else:
    best_ticker = "-"
    best_rate = 0

render_html(f"""
    <div class="header-card">
        <div style="display:flex; justify-content:space-between; align-items:start;">
            <div>
                <div class="market-badge">{market_text}</div>
                <h2 style="margin-top:5px; font-size:1.5rem; font-weight:800; line-height:1.2;">
                    {data_source.get('title', '배당 계산기')}
                </h2>
            </div>
            <div style="text-align:right;">
                <div style="font-weight:700;">1$ = {usd_krw:,.0f}원</div>
                <div style="font-size:0.7rem; opacity:0.8;">{update_time} 기준</div>
            </div>
        </div>
        <div style="display:flex; gap:10px; margin-top:20px; background:rgba(0,0,0,0.15); padding:12px; border-radius:12px;">
            <div style="flex:1; text-align:center;">
                <div style="font-size:0.7rem; opacity:0.8;">매수마감</div>
                <div style="font-weight:700; font-size:0.9rem;">{SCHEDULE_KST.get('buy_limit', '-')}</div>
            </div>
            <div style="flex:1; text-align:center; border-left:1px solid rgba(255,255,255,0.2);">
                <div style="font-size:0.7rem; opacity:0.8;">배당락일</div>
                <div style="font-weight:700; font-size:0.9rem;">{SCHEDULE_KST.get('ex_date', '-')}</div>
            </div>
            <div style="flex:1; text-align:center; border-left:1px solid rgba(255,255,255,0.2);">
                <div style="font-size:0.7rem; opacity:0.8;">지급일</div>
                <div style="font-weight:700; font-size:0.9rem; color:#fff;">{SCHEDULE_KST.get('pay_date', '-')}</div>
            </div>
        </div>
    </div>
""")

render_html(f"""
    <div class="hot-banner">
        <div style="display:flex; align-items:center; gap:8px;">
            <span style="background:#ef4444; color:white; padding:4px 8px; border-radius:8px; font-size:0.75rem; font-weight:800;">HOT 🔥</span>
            <span style="font-size:0.9rem; font-weight:700; color:#333;">최고 분배율 <span style="color:{THEME_COLORS[0]};">{best_ticker}</span></span>
        </div>
        <span style="color:{THEME_COLORS[0]}; font-weight:800; font-size:1rem;">{best_rate}%</span>
    </div>
""")

# ---------------------------------------------------------
# [UI 4] 종목 분석 및 계산기
# ---------------------------------------------------------
st.markdown("### 💎 종목별 상세 분석")
sel_ticker = st.selectbox("분석할 종목 선택", t_list)

if sel_ticker:
    d = DATA_MAP[sel_ticker]
    # 주가가 0.0이면 기본값 처리 (에러 방지)
    curr_p = price_map.get(sel_ticker, 0.0)
    if curr_p == 0.0:
        price_display = "데이터 없음"
        curr_p_calc = 0.0 # 계산용 (0으로 처리)
    else:
        price_display = f"${curr_p:.2f}"
        curr_p_calc = curr_p

    div_usd = d['div']
    div_krw = div_usd * usd_krw
    div_krw_net = div_krw * (1 - tax_rate)

    rate_disp = f"{d['rate']}%" if d['rate'] > 0 else "TBA"
    sec_disp = f"{d['sec']}%" if d['sec'] > 0 else "-"

    grade_badge = ""
    if d['rate'] >= 80: grade_badge = "<span class='grade-badge' style='background:#ffebee; color:#c62828;'>🔥 초고배당</span>"
    elif d['rate'] >= 40: grade_badge = "<span class='grade-badge' style='background:#fff3e0; color:#ef6c00;'>⚡ 고배당</span>"
    elif d['rate'] > 0: grade_badge = "<span class='grade-badge' style='background:#e8f5e9; color:#2e7d32;'>🍀 중배당</span>"

    render_html(f"""
        <div class="info-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                <div>
                    <span style="background:{THEME_COLORS[1]}; color:white; padding:4px 10px; border-radius:8px; font-weight:800; font-size:0.9rem;">{sel_ticker}</span>
                    {grade_badge}
                </div>
                <span style="font-size:0.8rem; color:#888;">{d['name']}</span>
            </div>
            <div style="text-align:center; padding: 10px 0;">
                <div style="font-size:0.85rem; color:{THEME_COLORS[0]}; font-weight:600;">1주당 확정 배당금</div>
                <div style="font-size:2.4rem; font-weight:900; color:{THEME_COLORS[0]}; letter-spacing:-1px; line-height:1;">${div_usd:.4f}</div>
                <div style="font-size:1.1rem; font-weight:700; margin-top:8px;">
                    <span style="color:#adb5bd;">(세전) {div_krw:,.0f}원</span> 
                    <span style="margin:0 6px; color:#ddd;">|</span> 
                    <span style="color:{THEME_COLORS[0]};">{div_krw_net:,.0f}원 (세후)</span>
                </div>
            </div>
            <div style="display:flex; gap:8px; margin-top:20px;">
                <div style="flex:1; background:#f8f9fa; border-radius:12px; padding:10px; text-align:center;">
                    <div style="font-size:0.7rem; color:#666;">분배율</div>
                    <div style="font-weight:800; color:#333;">{rate_disp}</div>
                </div>
                <div style="flex:1; background:#f8f9fa; border-radius:12px; padding:10px; text-align:center;">
                    <div style="font-size:0.7rem; color:#666;">SEC 수익률</div>
                    <div style="font-weight:800; color:#333;">{sec_disp}</div>
                </div>
                <div style="flex:1; background:#f8f9fa; border-radius:12px; padding:10px; text-align:center;">
                    <div style="font-size:0.7rem; color:#666;">ROC 비율</div>
                    <div style="font-weight:800; color:#ef4444;">{d['roc']}%</div>
                </div>
            </div>
            <div style="margin-top:16px; background:#f1f3f5; padding:8px 12px; border-radius:8px; display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.75rem; color:#666;">현재 주가 (15분 지연)</span>
                <span style="font-weight:700; color:#333;">{price_display}</span>
            </div>
        </div>
    """)

    if 'prev_tab' not in st.session_state: st.session_state.prev_tab = "💼 포트폴리오"
    menu_options = ["💼 포트폴리오", "🧮 배당금", "💧 물타기", "🧪 스트레스", "📉 원금회수", "🔥 FIRE", "⛄ 스노우볼"]

    st.write("")
    current_tab = st.radio("계산기 메뉴", menu_options, horizontal=True, label_visibility="collapsed")

    if current_tab != st.session_state.prev_tab:
        if "FIRE" in current_tab: st.balloons()
        elif "스노우볼" in current_tab: st.snow()
        st.session_state.prev_tab = current_tab

    st.write("")

    # [계산기 로직 - 계산 기준 박스 복구]
    if current_tab == "💼 포트폴리오":
        st.markdown(f"<h5 style='color:{THEME_COLORS[0]}'>💼 내 보유 종목 통합 계산</h5>", unsafe_allow_html=True)
        selected_tickers = st.multiselect("보유 중인 종목 선택", options=t_list, default=[sel_ticker])

        if selected_tickers:
            total_pre_krw = 0
            for t in selected_tickers:
                c_name, c_qty = st.columns([1, 1.3])
                with c_name:
                    st.markdown(f"**{t}**")
                    st.caption(f"1주 ${DATA_MAP[t]['div']:.4f}") 
                with c_qty:
                    qty = st.number_input(f"{t} 수량", min_value=0, value=100, step=10, key=f"qty_{t}", label_visibility="collapsed")
                t_div_val = DATA_MAP[t]['div']
                total_pre_krw += (t_div_val * qty * usd_krw)
                st.markdown("<hr style='margin:5px 0; border-top: 1px solid #eee;'>", unsafe_allow_html=True)

            total_post_krw = total_pre_krw * (1 - tax_rate)
            render_html(f"""
                <div class="calc-card-bg">
                    <div style="text-align:center;">
                        <div style="font-size:0.9rem; color:{THEME_COLORS[0]}; margin-bottom:8px; font-weight:600;">이번 주 예상 수령액 합계</div>
                        <div style="font-size:1.8rem; font-weight:800; color:{THEME_COLORS[0]};">{total_post_krw:,.0f}원</div>
                        <div style="font-size:0.85rem; color:#6b7280; margin-top:4px;">(세전 {total_pre_krw:,.0f}원)</div>
                    </div>
                </div>
                <div class="caution-box">
                    <span class="caution-header">📌 계산 기준</span>
                    • 환율: <b>{usd_krw:,.2f}원</b> (실시간) / 세율: 15.4%<br>
                    • 선택하신 종목들의 이번 배당금 총합입니다.
                </div>
            """)
        else:
            st.info("👆 위에서 보유 종목을 먼저 선택해주세요!")

    elif current_tab == "🧮 배당금":
        c1, c2 = st.columns([1, 1.5])
        with c1:
            st.write("") 
            shares = st.number_input("보유 수량", min_value=1, value=1000, step=10, key="cal_shares")
        with c2:
            val_pre = shares * div_krw
            val_tax = val_pre * tax_rate
            val_post = val_pre - val_tax
            render_html(f"""
                <div class="calc-card-bg">
                    <div class="calc-row"><span class="calc-label">세전 배당금</span><span class="calc-val">{val_pre:,.0f}원</span></div>
                    <div class="calc-row"><span class="calc-label">세금 (15.4%)</span><span class="calc-val" style="color:#e92c2c;">-{val_tax:,.0f}원</span></div>
                    <div class="calc-divider"></div>
                    <div class="calc-row"><span class="calc-total-label">실제 입금액</span><span class="calc-total-val">{val_post:,.0f}원</span></div>
                </div>
                <div class="caution-box">
                    <span class="caution-header">📌 계산 기준</span>
                    • 환율: <b>{usd_krw:,.2f}원</b> (실시간) / 세율: 15.4%<br>
                    • 이번 주 배당금 <b>${d['div']:.4f}</b>가 기준입니다.
                </div>
            """)

    elif current_tab == "💧 물타기":
        c1, c2 = st.columns(2)
        with c1:
            # 주가가 없으면 기본값 0.1로 처리
            def_price = curr_p_calc if curr_p_calc > 0 else 10.0
            my_avg = st.number_input("내 평단가($)", min_value=0.01, value=def_price*1.1, step=0.1, format="%.2f")
        with c2:
            my_qty = st.number_input("보유 수량", min_value=1, value=100, step=10, key="mul_qty")
        add_qty = st.number_input("추가 매수할 수량(주)", min_value=1, value=50, step=10)

        old_total = my_avg * my_qty
        new_total = old_total + (curr_p_calc * add_qty)
        new_avg = new_total / (my_qty + add_qty)
        if div_usd > 0:
            old_w = my_avg / div_usd
            new_w = new_avg / div_usd
            saved = old_w - new_w
        else:
            old_w, new_w, saved = 0, 0, 0

        render_html(f"""
            <div class="calc-card-bg">
                <div style="font-size:0.9rem; color:#666; margin-bottom:8px;">평단가 변화 (현재가 ${curr_p_calc:.2f} 매수)</div>
                <div style="font-size:1.3rem; font-weight:700; display:flex; align-items:center; gap:8px;">
                    ${my_avg:.2f} <span style="color:#ccc;">➔</span> <span style="color:{THEME_COLORS[0]};">${new_avg:.2f}</span>
                </div>
                <div style="background:#f8f9fa; border-radius:12px; padding:12px; margin-top:16px;">
                    <div style="font-size:0.85rem; color:{THEME_COLORS[0]}; font-weight:600;">🚀 원금 회수 기간 단축</div>
                    <div style="font-size:1rem; font-weight:700; color:{THEME_COLORS[0]}; margin-top:4px;">
                        {old_w:.1f}회 ➔ {new_w:.1f}회 <span style="color:#00c853;">(-{saved:.1f}회 단축)</span>
                    </div>
                </div>
            </div>
            <div class="caution-box">
                <span class="caution-header">📌 계산 기준</span>
                • 추가 매수: <b>${curr_p_calc:.2f}</b> 체결 가정<br>
                • 배당금 유지 시 원금 회수 횟수 감소를 계산합니다.
            </div>
        """)

    elif current_tab == "🧪 스트레스":
        s_qty = st.number_input("보유 수량", min_value=100, value=1000, step=100, key="str_qty")
        base_pay = s_qty * div_krw_net
        render_html(f"""
            <div class="calc-card-bg">
                <div class="calc-row" style="background:#f0fdfa; padding:10px; border-radius:8px; margin-bottom:15px;">
                    <span class="calc-label" style="font-weight:700;">⚡ 현재 유지 시</span>
                    <span class="calc-val" style="color:{THEME_COLORS[0]}; font-size:1.1rem;">{base_pay:,.0f}원</span>
                </div>
                <div class="calc-row"><span class="calc-label">📉 -10% 삭감</span><span class="calc-val">{base_pay*0.9:,.0f}원</span></div>
                <div class="calc-row"><span class="calc-label">📉 -30% 삭감</span><span class="calc-val">{base_pay*0.7:,.0f}원</span></div>
                <div class="calc-row"><span class="calc-label" style="color:#e92c2c;">📉 -50% 삭감</span><span class="calc-val" style="color:#e92c2c;">{base_pay*0.5:,.0f}원</span></div>
            </div>
            <div class="caution-box">
                <span class="caution-header">📌 계산 기준</span>
                • <b>세후(15.4% 공제)</b> 금액 기준입니다.<br>
                • 배당 삭감 시나리오를 미리 확인하여 리스크를 대비하세요.
            </div>
        """)

    elif current_tab == "📉 원금회수":
        # 주가가 0이면 10.0으로 기본 설정
        def_val = curr_p_calc if curr_p_calc > 0 else 10.0
        bep_price = st.number_input("내 평단가($)", min_value=0.1, value=def_val, step=0.1, format="%.2f", key="bep_p")

        if div_usd > 0:
            w_need = bep_price / div_usd
            w_need = max(0, w_need)
            is_weekly = "Weekly" in data_source.get('title', "")
            m_need = w_need / 4.3 if is_weekly else w_need
        else:
            w_need, m_need = 0, 0
        render_html(f"""
            <div class="calc-card-bg" style="text-align:center;">
                <div style="font-size:0.9rem; color:#666; margin-bottom:8px;">원금 회수(Free Ride)까지</div>
                <div style="font-size:2rem; font-weight:900; color:#e92c2c; letter-spacing:-1px;">
                    {w_need:.1f}회 <span style="font-size:1rem; color:#999; font-weight:500;">(약 {m_need:.1f}개월)</span>
                </div>
            </div>
            <div class="caution-box">
                <span class="caution-header">📌 계산 기준</span>
                • 현재 배당금 <b>${div_usd:.4f}</b>가 유지된다는 가정입니다.<br>
                • 배당금만으로 투자 원금을 전액 회수하는 기간입니다.
            </div>
        """)

    elif current_tab == "🔥 FIRE":
        target = st.number_input("목표 배당금 (만원)", min_value=10, value=50, step=10)
        period_text = "매주" if "Weekly" in data_source.get('title', "") else "매월"
        if div_krw_net > 0:
            req_shares = math.ceil((target*10000) / div_krw_net)
            req_money = req_shares * curr_p_calc * usd_krw
        else:
            req_shares, req_money = 0, 0
        render_html(f"""
            <div class="calc-card-bg">
                <div style="text-align:center; margin-bottom:16px;">
                    <div style="font-size:0.9rem; color:#666;">{period_text} <b style="color:{THEME_COLORS[0]};">{target}만원</b> 받으려면?</div>
                </div>
                <div style="display:flex; justify-content:space-around; align-items:center;">
                    <div style="text-align:center;">
                        <div style="font-size:0.8rem; color:#888;">필요 주식</div>
                        <div style="font-size:1.2rem; font-weight:800; color:#333;">{req_shares:,}주</div>
                    </div>
                    <div style="width:1px; height:30px; background:#eee;"></div>
                    <div style="text-align:center;">
                        <div style="font-size:0.8rem; color:#888;">예상 투자금</div>
                        <div style="font-size:1.2rem; font-weight:800; color:{THEME_COLORS[0]};">{req_money/10000:,.0f}만원</div>
                    </div>
                </div>
            </div>
            <div class="caution-box">
                <span class="caution-header">📌 계산 기준</span>
                • 환율: <b>{usd_krw:,.2f}원</b> / 현재가: <b>${curr_p_calc:.2f}</b><br>
                • 세후 배당금을 기준으로 역산한 결과입니다.
            </div>
        """)

    elif current_tab == "⛄ 스노우볼":
        snow_shares = st.number_input("현재 보유 수량", min_value=1, value=1000, step=10, key="snow_s")
        this_pay = snow_shares * div_krw_net
        re_price = curr_p_calc * usd_krw
        if re_price > 0:
            add_cnt = math.floor(this_pay / re_price)
            rem_cash = this_pay - (add_cnt * re_price)
            next_inc = add_cnt * div_krw_net
        else:
            add_cnt, rem_cash, next_inc = 0, 0, 0
        render_html(f"""
            <div class="calc-card-bg" style="background:linear-gradient(135deg, #f8f9fa 0%, #fff 100%);">
                <div style="text-align:center; margin-bottom:10px;">
                    <span style="font-size:0.9rem; color:#555;">이번 배당금으로</span><br>
                    <span style="font-size:1.5rem; font-weight:900; color:{THEME_COLORS[0]};">+{add_cnt}주</span>
                    <span style="font-size:1rem; font-weight:700;"> 추가 매수!</span>
                </div>
                <div style="background:white; border-radius:12px; padding:12px; text-align:center; border:1px solid #eee;">
                    <div style="font-size:0.8rem; color:#888;">재투자로 늘어나는 다음 배당금</div>
                    <div style="font-size:1.1rem; font-weight:800; color:{THEME_COLORS[0]};">+{next_inc:,.0f}원 🆙</div>
                </div>
            </div>
            <div class="caution-box">
                <span class="caution-header">📌 계산 기준</span>
                • 재투자 단가: <b>${curr_p_calc:.2f}</b> (현재가)<br>
                • 배당금 삭감 없이 세후 금액 전액 재투자 가정
            </div>
        """)

    # 6. 하단 FAQ
    st.write("")
    st.markdown("##### 🧐 주린이가 자주 묻는 질문")

    with st.expander("Q. 배당금은 언제 들어오나요?"):
        st.info("미국 현지 지급일(Pay Date)로부터 증권사 입금까지 **보통 2~3 영업일**이 더 소요됩니다. 조금만 기다려주세요! 🕒")

    with st.expander("Q. ROC가 뭔가요? (중요 ⚠️)"):
        st.warning("""
        **Return of Capital (투자 원금 반환)**

        펀드가 이익을 내서 주는 돈이 아니라, **여러분의 원금을 깎아서** 배당으로 주는 것을 말합니다.
        - 장점: 당장 내야 할 배당소득세가 없을 수 있습니다.
        - 단점: 내 평단가가 그만큼 낮아져서, 나중에 주식을 팔 때 양도세가 커질 수 있습니다.
        """)

    with st.expander("Q. 환율은 어떻게 적용되나요?"):
        st.write(f"""
        이 앱은 현재 실시간 환율(**{usd_krw:,.0f}원**)을 기준으로 계산합니다. 
        실제 입금 시점의 환율에 따라 금액이 달라질 수 있습니다.
        """)