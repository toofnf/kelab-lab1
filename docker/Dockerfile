ARG PROJECT_DIR=/project
ARG PYTHON_BASE_VERSION=3.10

FROM python:${PYTHON_BASE_VERSION}-slim-buster as base_downloader

# Обновляем список пакетов и устанавливаем Curl с помощью командной строки
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

FROM base_downloader AS pdm_downloader

ARG PROJECT_DIR
ARG PDM_VERSION=2.10.0
COPY --from=base_downloader /usr/bin/curl /usr/bin/curl
RUN curl -sSL https://pdm.fming.dev/install-pdm.py | python - --version="${PDM_VERSION}"

FROM pdm_downloader as pdm_builder
# copy files
COPY --from=pdm_downloader /root/.local/bin/pdm /usr/bin/pdm
COPY pyproject.toml pdm.lock ${PROJECT_DIR}/

# install dependencies and project into the local packages directory
WORKDIR ${PROJECT_DIR}
RUN mkdir __pypackages__ && pdm sync --prod --no-editable

# run stage

FROM python:${PYTHON_BASE_VERSION}-slim-buster
ARG PYTHON_BASE_VERSION
ARG PROJECT_DIR
# retrieve packages from build stage
ENV PYTHONPATH=${PROJECT_DIR}/pkgs
COPY --from=pdm_builder ${PROJECT_DIR}/__pypackages__/${PYTHON_BASE_VERSION}/lib ${PROJECT_DIR}/pkgs

# retrieve executables
COPY --from=pdm_builder ${PROJECT_DIR}/__pypackages__/${PYTHON_BASE_VERSION}/bin/* /bin/
COPY src/main.py src/main.py
# set command/entrypoint, adapt to fit your needs
CMD ["python", "-m", "uvicorn", "src.main:app", "--port", "9000", "--host", "0.0.0.0"]