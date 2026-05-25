# Holographic Duality (AdS/CFT) Engine for ETFs

Applies the AdS/CFT correspondence (Maldacena 1997) to ETF correlation graphs. The market is the boundary CFT; the bulk is a black hole geometry. Each ETF’s **geodesic distance** to the graph center is interpreted as a measure of quantum entanglement – a novel structural signal.

## Features
- Three ETF universes (FI/Commodities, Equity Sectors, Combined)
- Seven rolling windows (63–4536 days)
- Graph from distance matrix = 1 - |correlation|
- Graph center determined by closeness centrality
- Geodesic length = shortest path distance to center
- Best window automatically selected (largest raw geodesic length)
- Two‑tab Streamlit dashboard (auto best + manual window selection)
- Results stored on Hugging Face: `P2SAMAPA/p2-etf-holographic-duality-results`

## Usage

1. Set `HF_TOKEN` environment variable.
2. Run training: `python train.py`
3. Launch dashboard: `streamlit run streamlit_app.py`
4. GitHub Actions runs daily.

## Interpretation

- **AdS/CFT** maps strongly coupled quantum systems to classical gravity.
- The geodesic distance in the bulk is dual to the entanglement entropy of a boundary region.
- ETFs far from the center are more “entangled” with the rest – potentially systemic or alpha‑rich.
- This is a completely novel application of holographic duality to finance.

## Requirements

See `requirements.txt`.
