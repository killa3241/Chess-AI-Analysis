export const analyzePGN = async (file: File): Promise<string[]> => {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      body: formData,
    });
    const result = await response.json();
    return result.advice || []; // return empty array if no advice
  } catch (err) {
    console.error("API call failed:", err);
    return [];
  }
};
