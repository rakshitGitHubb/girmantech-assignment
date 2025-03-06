<template>
  <div class="relative min-h-screen">
    <div
      class="absolute inset-0 bg-no-repeat bg-cover bg-center"
      style="background-image: url('/girman_preview.jpg'); image-rendering: crisp-edges;"
    ></div>
    <div class="absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-purple-100 to-transparent"></div>

    <div class="relative z-10 flex flex-col min-h-screen">
      <header class="w-full py-4 px-6 border-b border-gray-300 shadow-md">
        <div class="container mx-auto flex items-center justify-between">
          <router-link to="/" class="flex items-center">
            <img src="/gtlogo.png" alt="Girman Technologies" class="h-14" />
          </router-link>
          <nav class="hidden sm:flex items-center space-x-6 text-sm">
            <router-link
              to="/"
              :class="[
                'border-b-4 px-2 pb-1 uppercase transition-colors',
                isHomeRoute ? 'text-blue-600 border-blue-600 font-semibold' : 'text-gray-600 border-transparent hover:text-blue-500'
              ]"
            >
              SEARCH
            </router-link>
            <a
              href="https://girmantech.com"
              target="_blank"
              class="text-gray-600 hover:text-blue-500 transition-colors uppercase border-b-4 border-transparent px-2 pb-1"
            >
              WEBSITE
            </a>
            <a
              href="https://www.linkedin.com/company/girmantech"
              target="_blank"
              class="text-gray-600 hover:text-blue-500 transition-colors uppercase border-b-4 border-transparent px-2 pb-1"
            >
              LINKEDIN
            </a>
            <a
              href="mailto:contact@girmantech.com"
              class="text-gray-600 hover:text-blue-500 transition-colors uppercase border-b-4 border-transparent px-2 pb-1"
            >
              CONTACT
            </a>
          </nav>
          <button
            @click="toggleMobileMenu"
            class="sm:hidden text-gray-600 hover:text-blue-500 focus:outline-none"
          >
            <svg
              class="h-6 w-6"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              viewBox="0 0 24 24"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
        <transition name="fade">
          <div
            v-if="mobileMenuOpen"
            class="sm:hidden bg-white border-t border-gray-300 shadow px-6 py-4"
          >
            <router-link
              to="/"
              class="block text-gray-600 hover:text-blue-500 uppercase mb-2 border-b-4 border-transparent pb-1"
              :class="isHomeRoute ? 'text-blue-600 border-blue-600 font-semibold' : ''"
              @click="toggleMobileMenu"
            >
              SEARCH
            </router-link>
            <a
              href="https://girmantech.com"
              target="_blank"
              class="block text-gray-600 hover:text-blue-500 uppercase mb-2 border-b-4 border-transparent pb-1"
              @click="toggleMobileMenu"
            >
              WEBSITE
            </a>
            <a
              href="https://www.linkedin.com/company/girmantech"
              target="_blank"
              class="block text-gray-600 hover:text-blue-500 uppercase mb-2 border-b-4 border-transparent pb-1"
              @click="toggleMobileMenu"
            >
              LINKEDIN
            </a>
            <a
              href="mailto:contact@girmantech.com"
              class="block text-gray-600 hover:text-blue-500 uppercase border-b-4 border-transparent pb-1"
              @click="toggleMobileMenu"
            >
              CONTACT
            </a>
          </div>
        </transition>
      </header>

      <main
        class="flex-grow flex flex-col items-center px-4 transition-all duration-300"
        :class="hasSearched ? 'justify-start pt-12' : 'justify-center'"
      >
        <div class="relative w-full max-w-2xl mt-4">
          <input
            type="text"
            v-model="searchTerm"
            @keyup.enter="performSearch"
            placeholder="Search..."
            class="w-full p-4 border border-gray-300 rounded-full shadow-xl 
                   focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-150"
          />
        </div>

        <div v-if="hasSearched" class="w-full max-w-2xl mt-8 flex flex-col items-center">
          <div v-if="loading" class="text-gray-600 mt-4">Loading...</div>
          <div v-else-if="results.length === 0" class="flex flex-col items-center mt-8">
            <img
              :src="noResultsImage"
              alt="No results"
              class="mb-4 w-full object-cover blended-edge"
            />
            <p class="text-gray-500">No results found.</p>
          </div>
          <div v-else class="grid grid-cols-1 sm:grid-cols-2 gap-6 mt-6 w-full">
            <div
              v-for="(user, index) in results"
              :key="index"
              class="bg-white p-4 rounded-lg shadow-md flex flex-col items-center w-full"
            >
              <img
                :src="user.profile_image || '/userimage.png'"
                alt="User Image"
                class="w-16 h-16 rounded-full object-cover mb-2"
              />
              <p class="font-semibold text-gray-800">
                {{ user.first_name }} {{ user.last_name }}
              </p>
              <p class="text-gray-500 text-sm">{{ user.city }}</p>
              <p class="text-gray-500 text-sm">{{ user.contact_number }}</p>
              <button
                @click="openDetails(user)"
                class="mt-4 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded transition"
              >
                Fetch Details
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>

    <button
      class="fixed bottom-4 right-4 w-16 h-16 rounded-full bg-blue-500 hover:bg-blue-600 text-white flex items-center justify-center shadow-xl z-50 group"
      @click="toggleChatbot"
    >
      <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 20 20">
        <path d="M18 10c0 3.866-3.582 7-8 7a8.15 8.15 0 01-3.514-.76L2 17l1.764-4.486A7.965 7.965 0 012 10c0-3.866 3.582-7 8-7s8 3.134 8 7z" />
      </svg>
      <span class="absolute bottom-full mb-2 hidden group-hover:block text-xs bg-gray-700 text-white px-2 py-1 rounded">Need some help?</span>
    </button>

    <transition name="fade">
      <div
        v-if="chatbotOpen"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
      >
        <div class="bg-white w-11/12 max-w-md p-6 rounded shadow-lg relative">
          <button
            @click="toggleChatbot"
            class="absolute top-2 right-2 text-gray-400 hover:text-gray-600 text-xl"
          >
            &times;
          </button>
          <h2 class="text-xl font-bold mb-4">Chatbot Assistant</h2>
          <div class="h-64 overflow-y-auto border p-2 mb-4">
            <div v-for="(msg, idx) in chatHistory" :key="idx" class="mb-2">
              <p :class="msg.sender === 'user' ? 'text-right text-blue-600' : 'text-left text-gray-800'">
                <span v-if="msg.sender === 'user'">You: </span>
                <span v-else>Bot: </span>
                {{ msg.message }}
              </p>
            </div>
          </div>
          <input
            type="text"
            v-model="chatMessage"
            placeholder="Type your message..."
            class="w-full p-2 border rounded"
            @keyup.enter="sendChatMessage"
          />
        </div>
      </div>
    </transition>

    <transition name="fade">
      <div
        v-if="showModal"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
      >
        <div class="backdrop-blur-sm absolute inset-0"></div>
        <div class="bg-white w-11/12 max-w-md p-6 rounded shadow-lg relative z-10">
          <button
            @click="closeModal"
            class="absolute top-2 right-2 text-gray-400 hover:text-gray-600 text-xl"
          >
            &times;
          </button>
          <h2 class="text-xl font-bold mb-2">Fetch Details</h2>
          <p class="text-gray-600 mb-2">Here are the details of the selected employee.</p>
          <p class="font-semibold">
            Name: {{ selectedUser.first_name }} {{ selectedUser.last_name }}
          </p>
          <p>Location: {{ selectedUser.city }}</p>
          <p>Contact Number: {{ selectedUser.contact_number }}</p>
          <p class="mt-2"><strong>Profile Image:</strong></p>
          <img
            :src="selectedUser.profile_image || '/userimage.png'"
            alt="User Image"
            class="w-32 h-32 object-cover rounded mt-2"
          />
          <button
            @click="closeModal"
            class="mt-4 bg-gray-300 hover:bg-gray-400 text-gray-800 px-4 py-2 rounded transition"
          >
            Close
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomePage',
  data() {
    return {
      searchTerm: '',
      results: [],
      loading: false,
      hasSearched: false,

      showModal: false,
      selectedUser: {},
      placeholderImage: 'https://via.placeholder.com/150',

      mobileMenuOpen: false,

      chatbotOpen: false,
      chatMessage: '',
      chatHistory: [],

      noResultsImage: '/noresults.jpg'
    }
  },
  computed: {
    isHomeRoute() {
      return this.$route.name === 'Home'
    }
  },
  methods: {
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen
    },
    async performSearch() {
      if (!this.searchTerm.trim()) return
      this.hasSearched = true
      this.loading = true
      this.results = []
      try {
        const response = await axios.get('/api/method/gt_assignment.api.get_user_data', {
          params: { search_term: this.searchTerm.trim() }
        })
        this.results = response.data.message || []
      } catch (error) {
        console.error('Error fetching data:', error)
      } finally {
        this.loading = false
      }
    },
    openDetails(user) {
      this.selectedUser = user
      this.showModal = true
    },
    closeModal() {
      this.showModal = false
      this.selectedUser = {}
    },
    toggleChatbot() {
      this.chatbotOpen = !this.chatbotOpen
    },
    sendChatMessage() {
      if (!this.chatMessage.trim()) return
      this.chatHistory.push({ sender: 'user', message: this.chatMessage.trim() })
      const userMsg = this.chatMessage.trim()
      this.chatMessage = ''
      let reply = "I'm sorry, I didn't understand that."
      const lowerMsg = userMsg.toLowerCase()
      if (lowerMsg.includes('youtube')) {
        reply = "Redirecting to YouTube..."
        window.location.href = 'https://www.youtube.com'
      } else if (lowerMsg.includes('wikipedia')) {
        reply = "Redirecting to Wikipedia..."
        window.location.href = 'https://www.wikipedia.org'
      } else if (lowerMsg.includes('google')) {
        reply = "Redirecting to Google..."
        window.location.href = 'https://www.google.com'
      } else if (lowerMsg.includes('hi') || lowerMsg.includes('hello')) {
        reply = "Hello! How can I help you?"
      } else if (lowerMsg.includes('how are you')) {
        reply = "I'm good, thank you! How can I assist you today?"
      }
      if (!reply.startsWith("Redirecting")) {
        this.chatHistory.push({ sender: 'bot', message: reply })
      }
    }
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.backdrop-blur-sm {
  backdrop-filter: blur(5px);
}

.blended-edge {
  mask-image: radial-gradient(circle at center, black 60%, transparent 100%);
  mask-size: cover;
  mask-repeat: no-repeat;

  -webkit-mask-image: radial-gradient(circle at center, black 60%, transparent 100%);
  -webkit-mask-size: cover;
  -webkit-mask-repeat: no-repeat;
}
</style>
