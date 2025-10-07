<template>
  <div class="dashboard">
    <header class="bg-white shadow-sm border-b">
      <div class="max-w-7xl mx-auto px-4 py-4">
        <h1 class="text-2xl font-bold text-gray-900">Dashboard</h1>
      </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 py-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div class="bg-white p-6 rounded-lg shadow-sm border">
          <h3 class="text-lg font-semibold text-gray-700">Total Contacts</h3>
          <p class="text-3xl font-bold text-blue-600">0</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border">
          <h3 class="text-lg font-semibold text-gray-700">Active Deals</h3>
          <p class="text-3xl font-bold text-green-600">0</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border">
          <h3 class="text-lg font-semibold text-gray-700">Pipeline Value</h3>
          <p class="text-3xl font-bold text-purple-600">$0</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border">
          <h3 class="text-lg font-semibold text-gray-700">Conversion Rate</h3>
          <p class="text-3xl font-bold text-orange-600">0%</p>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-sm border">
        <h2 class="text-xl font-semibold mb-4">Welcome to NexusCRM</h2>
        <p class="text-gray-600">Your modern CRM platform is ready for development!</p>
      </div>
    </main>
  </div>
</template>

<script setup>
</script>
