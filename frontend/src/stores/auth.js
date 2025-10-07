import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('token'))
  
  const isAuthenticated = computed(() => !!token.value)
  
  function setAuth(userData, authToken) {
    user.value = userData
    token.value = authToken
    localStorage.setItem('token', authToken)
    axios.defaults.headers.common['Authorization'] = `Bearer ${authToken}`
  }
  
  async function login(credentials) {
    try {
      // TODO: Replace with actual API call
      const response = { data: { user: { name: 'Test User' }, token: 'test-token' } }
      setAuth(response.data.user, response.data.token)
      return response.data
    } catch (error) {
      throw error
    }
  }
  
  return {
    user,
    token,
    isAuthenticated,
    login
  }
})
