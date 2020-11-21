#!/usr/bin/env node

const cdk = require('@aws-cdk/core');
const { C02PythonWordPdfFargateStack } = require('./stacks/c-02-python-word-pdf-fargate-stack');

const app = new cdk.App();
new C02PythonWordPdfFargateStack(app, 'C02-PYTHON-WORD-PDF-FARGATE-Stack');
