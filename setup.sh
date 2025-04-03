mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = truen\n\
\n\
" > ~/.streamlit/config.toml