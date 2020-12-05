mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"johanneseboigbe55@yahoo.com.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
