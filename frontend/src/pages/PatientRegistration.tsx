import React, { useState } from 'react';

interface Patient {
  firstName: string;
  lastName: string;
  email: string;
  // Add other fields as needed
}

const PatientRegistration: React.FC = () => {
  const [patient, setPatient] = useState<Patient>({ firstName: '', lastName: '', email: '' });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPatient({ ...patient, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission (e.g., API call)
    console.log('Patient data:', patient);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="firstName" value={patient.firstName} onChange={handleChange} placeholder="First Name" required/>
      <input type="text" name="lastName" value={patient.lastName} onChange={handleChange} placeholder="Last Name" required/>
      <input type="email" name="email" value={patient.email} onChange={handleChange} placeholder="Email" required/>
      <button type="submit">Register</button>
    </form>
  );
};

export default PatientRegistration;