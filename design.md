# Multi-Agent Resume Screening System

## Overview
A sophisticated resume screening system that uses multiple AI agents to analyze job descriptions and evaluate candidate resumes.

## Features
- Support for PDF and DOCX document conversion
- Intelligent job description analysis
- Resume information extraction using NLP
- ML-based candidate evaluation using LLM
- RESTful API interface

## System Architecture
The system consists of four main agents:

1. **Document Converter Agent**
   - Converts PDF and DOCX files to text.

2. **Knowledge Extractor Agent**
   - Uses NLP to extract key information from resumes (skills, education, work experience).

3. **Decision Maker Agent**
   - Evaluates candidates against structured job requirements.

4. **JD Analyzer Agent**
   - Analyzes job descriptions and structured requirements.

## Technologies Used
- **Python** with FastAPI for backend processing
- **PDF parsing API** for document extraction
- **Streamlit** for frontend UI
- **OpenAI GPT/Llama3 API** for NLP and ML processing

## Workflow
1. Upload resume and job description (PDF or DOCX)
2. Convert documents to text
3. Extract key information from resumes and job descriptions
4. Evaluate candidates using an ML model
5. Display results via API and frontend UI

## API Endpoints

| Method | Endpoint | Description |
|--------|--------------------|----------------------|
| POST   | /upload_resume     | Upload resume PDF/DOCX |
| POST   | /upload_jd         | Upload job description |
| POST   | /evaluate_candidate | Run candidate matching |

## Deployment
The system is designed for local deployment and can be containerized for production use.

## LLM use openai client
base_url = "http://10.4.33.13:80/v1 "
model_name = "ibnzterrell/Meta-Llama-3.3-70B-Instruct-AWQ-INT4"
api_key = "123"

## Tool to convert pdf to markdown 
```
import aiohttp
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class PDFParserAgent:
    """Agent responsible for parsing PDF documents using external API."""
    
    def __init__(self, api_url: str = "http://10.2.3.50:8000/parse_document/pdf"):
        self.api_url = api_url
        
    async def parse_pdf(self, pdf_content: bytes) -> Dict[str, Any]:
        """
        Parse PDF content using the external API.
        
        Args:
            pdf_content: The binary content of the PDF file
            
        Returns:
            Dict containing the parsed PDF data
        """
        try:
            async with aiohttp.ClientSession() as session:
                form = aiohttp.FormData()
                form.add_field('file',
                             pdf_content,
                             filename='document.pdf',
                             content_type='application/pdf')
                
                async with session.post(self.api_url, data=form) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        error_text = await response.text()
                        logger.error(f"PDF parsing failed with status {response.status}: {error_text}")
                        raise Exception(f"PDF parsing failed: {error_text}")
                        
        except Exception as e:
            logger.error(f"Error parsing PDF: {str(e)}")
            raise 
```