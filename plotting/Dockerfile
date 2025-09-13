FROM texlive/texlive:latest

# Install LaTeX packages and system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-pygments
RUN tlmgr update --self && tlmgr install latexmk minted


WORKDIR /doc
