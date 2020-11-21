#!/usr/bin/env node

const cdk = require('@aws-cdk/core');
const { C02PythonWordPdfEcrStack } = require('./stacks/c-02-python-word-pdf-ecr-stack');

const app = new cdk.App();
new C02PythonWordPdfEcrStack(app, 'C02-PYTHON-WORD-PDF-ECR-Stack');
