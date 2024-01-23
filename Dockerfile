FROM public.ecr.aws/spacelift/runner-terraform:latest

USER root
RUN apk add --no-cache nodejs npm python3
RUN npm install --global cdktf-cli@latest
RUN python3 -m ensurepip \
  && python3 -m pip install --upgrade pip setuptools

USER spacelift
RUN pip3 install --user pipenv
ENV PATH="/home/spacelift/.local/bin:$PATH"