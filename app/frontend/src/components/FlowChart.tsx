import React, { useEffect, useRef } from 'react';
import mermaid from 'mermaid';
import { Box, Paper } from '@mui/material';

interface FlowChartProps {
  steps: {
    id: string;
    title: string;
    description: string;
    status: 'pending' | 'running' | 'completed' | 'error';
    details?: string;
  }[];
}

const FlowChart: React.FC<FlowChartProps> = ({ steps }) => {
  const chartRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!chartRef.current) return;

    // 初始化 Mermaid
    mermaid.initialize({
      startOnLoad: true,
      theme: 'default',
      securityLevel: 'loose',
      flowchart: {
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis',
      },
    });

    // 生成流程图定义
    const flowchartDefinition = generateFlowchartDefinition(steps);

    // 渲染流程图
    mermaid.render('flowchart', flowchartDefinition).then(({ svg }) => {
      if (chartRef.current) {
        chartRef.current.innerHTML = svg;
      }
    });
  }, [steps]);

  const generateFlowchartDefinition = (steps: FlowChartProps['steps']): string => {
    // 定义节点样式
    const getNodeStyle = (status: string) => {
      switch (status) {
        case 'completed':
          return 'fill:#4CAF50,stroke:#2E7D32,stroke-width:2px';
        case 'running':
          return 'fill:#2196F3,stroke:#1565C0,stroke-width:2px';
        case 'error':
          return 'fill:#F44336,stroke:#C62828,stroke-width:2px';
        default:
          return 'fill:#E0E0E0,stroke:#9E9E9E,stroke-width:1px';
      }
    };

    // 生成节点定义
    const nodes = steps.map((step, index) => {
      const nodeId = `node${index + 1}`;
      const style = getNodeStyle(step.status);
      return `${nodeId}["${step.title}<br/>${step.description}"]:::${step.status}`;
    }).join('\n');

    // 生成连接线定义
    const connections = steps.slice(0, -1).map((_, index) => {
      const fromNode = `node${index + 1}`;
      const toNode = `node${index + 2}`;
      return `${fromNode} --> ${toNode}`;
    }).join('\n');

    // 组合完整的流程图定义
    return `
      graph TD
        classDef pending fill:#E0E0E0,stroke:#9E9E9E,stroke-width:1px
        classDef running fill:#2196F3,stroke:#1565C0,stroke-width:2px
        classDef completed fill:#4CAF50,stroke:#2E7D32,stroke-width:2px
        classDef error fill:#F44336,stroke:#C62828,stroke-width:2px
        
        ${nodes}
        ${connections}
    `;
  };

  return (
    <Box sx={{ width: '100%', height: '100%', overflow: 'auto' }}>
      <Paper sx={{ p: 2, height: '100%' }}>
        <div ref={chartRef} style={{ width: '100%', height: '100%' }} />
      </Paper>
    </Box>
  );
};

export default FlowChart; 