import React, { useState } from 'react';
import PropTypes from 'prop-types';

// Component for this project.
const Construction = ({ projectName, status, onUpdate }) => {
  const [progress, setProgress] = useState(0);

  const handleProgressChange = (e) => {
    const newProgress = parseInt(e.target.value, 10);
    setProgress(newProgress);
    if (onUpdate) onUpdate(newProgress);
  };

  return (
    <div className="construction-card">
      <h2>{projectName}</h2>
      <p>Status: <strong>{status}</strong></p>
      <label htmlFor="progress">Progress: {progress}%</label>
      <input
        type="range"
        id="progress"
        min="0"
        max="100"
        value={progress}
        onChange={handleProgressChange}
      />
    </div>
  );
};

Construction.propTypes = {
  projectName: PropTypes.string.isRequired,
  status: PropTypes.string,
  onUpdate: PropTypes.func,
};

Construction.defaultProps = {
  status: 'Planning',
  onUpdate: null,
};

export default Construction;