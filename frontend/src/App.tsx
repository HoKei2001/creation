import React, { useState, useEffect } from 'react';
import {
  Container,
  Box,
  TextField,
  Button,
  Paper,
  Typography,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  CircularProgress,
} from '@mui/material';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

interface ModelInfo {
  id: string;
  name: string;
  description: string;
}

function App() {
  const [prompt, setPrompt] = useState('');
  const [language, setLanguage] = useState('python');
  const [model, setModel] = useState('');
  const [models, setModels] = useState<ModelInfo[]>([]);
  const [generatedCode, setGeneratedCode] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Fetch available models
    const fetchModels = async () => {
      try {
        const response = await axios.get(`${API_URL}/models`);
        setModels(response.data);
        if (response.data.length > 0) {
          setModel(response.data[0].id);
        }
      } catch (err) {
        console.error('Failed to fetch models:', err);
      }
    };

    fetchModels();
  }, []);

  const handleGenerate = async () => {
    try {
      setLoading(true);
      setError('');
      const response = await axios.post(`${API_URL}/generate`, {
        prompt,
        language,
        model,
      });
      setGeneratedCode(response.data.code);
      setOutput(response.data.output);
    } catch (err) {
      setError('Failed to generate code');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleExecute = async () => {
    try {
      setLoading(true);
      setError('');
      const response = await axios.post(`${API_URL}/execute`, {
        prompt: generatedCode,
        language,
      });
      setOutput(response.data.output);
      if (response.data.error) {
        setError(response.data.error);
      }
    } catch (err) {
      setError('Failed to execute code');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Code Generation Platform
        </Typography>

        <Paper sx={{ p: 3, mb: 3 }}>
          <FormControl fullWidth sx={{ mb: 2 }}>
            <InputLabel>Model</InputLabel>
            <Select
              value={model}
              label="Model"
              onChange={(e) => setModel(e.target.value)}
            >
              {models.map((modelInfo) => (
                <MenuItem key={modelInfo.id} value={modelInfo.id}>
                  {modelInfo.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <FormControl fullWidth sx={{ mb: 2 }}>
            <InputLabel>Programming Language</InputLabel>
            <Select
              value={language}
              label="Programming Language"
              onChange={(e) => setLanguage(e.target.value)}
            >
              <MenuItem value="python">Python</MenuItem>
              <MenuItem value="javascript">JavaScript</MenuItem>
              <MenuItem value="java">Java</MenuItem>
            </Select>
          </FormControl>

          <TextField
            fullWidth
            multiline
            rows={4}
            label="Enter your prompt"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            sx={{ mb: 2 }}
          />

          <Box sx={{ display: 'flex', gap: 2 }}>
            <Button
              variant="contained"
              onClick={handleGenerate}
              disabled={loading || !prompt}
            >
              Generate Code
            </Button>
            <Button
              variant="contained"
              color="secondary"
              onClick={handleExecute}
              disabled={loading || !generatedCode}
            >
              Execute Code
            </Button>
          </Box>
        </Paper>

        {loading && (
          <Box sx={{ display: 'flex', justifyContent: 'center', my: 2 }}>
            <CircularProgress />
          </Box>
        )}

        {generatedCode && (
          <Paper sx={{ p: 3, mb: 3 }}>
            <Typography variant="h6" gutterBottom>
              Generated Code
            </Typography>
            <TextField
              fullWidth
              multiline
              rows={6}
              value={generatedCode}
              InputProps={{ readOnly: true }}
            />
          </Paper>
        )}

        {output && (
          <Paper sx={{ p: 3, mb: 3 }}>
            <Typography variant="h6" gutterBottom>
              Output
            </Typography>
            <TextField
              fullWidth
              multiline
              rows={4}
              value={output}
              InputProps={{ readOnly: true }}
            />
          </Paper>
        )}

        {error && (
          <Paper sx={{ p: 3, bgcolor: '#ffebee' }}>
            <Typography color="error">{error}</Typography>
          </Paper>
        )}
      </Box>
    </Container>
  );
}

export default App; 