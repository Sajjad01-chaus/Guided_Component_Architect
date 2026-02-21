'use client'

import { useState } from 'react'

export default function Home() {
  const [prompt, setPrompt] = useState('')
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  const generate = async () => {
    try {
      setLoading(true)

      const res = await fetch(
        process.env.NEXT_PUBLIC_API_URL + '/generate',
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt })
        }
      )

      if (!res.ok) {
        throw new Error('API request failed')
      }

      const data = await res.json()
      setResult(data)
    } catch (err) {
      console.error(err)
      alert('Something went wrong.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="min-h-screen bg-gray-900 text-white p-10">
      <h1 className="text-3xl font-bold mb-6">
        Guided Component Architect
      </h1>

      <textarea
        className="w-full p-3 bg-white text-black rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        rows={4}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Describe your component..."
      />

      <button
        onClick={generate}
        className="mt-4 px-6 py-2 bg-indigo-600 rounded hover:bg-indigo-700"
      >
        {loading ? 'Generating...' : 'Generate'}
      </button>

      {result && (
        <div className="mt-10 p-6 bg-gray-800 rounded">
          <h2 className="text-xl mb-4">Live Preview</h2>

          {/* Inject generated CSS */}
          <style>{result.css}</style>

          {/* Render generated HTML */}
          <div
            dangerouslySetInnerHTML={{ __html: result.html }}
          />
        </div>
      )}
    </main>
  )
}