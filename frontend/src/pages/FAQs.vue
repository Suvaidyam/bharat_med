<template>
	<div class="bg-gradient-to-br from-gray-100 to-gray-200 relative overflow-hidden">
		<!-- Background Image Overlay -->
		<div
			class="absolute inset-0 bg-cover bg-center opacity-20"
			style="background-image: url('/api/placeholder/1920/1080')"
		/>

		<!-- Medical Equipment Decorative Elements -->
		<div class="absolute top-20 right-10 opacity-30 hidden lg:block">
			<div
				class="w-32 h-32 rounded-full border-4 border-blue-400 flex items-center justify-center"
			>
				<div class="w-16 h-16 bg-blue-400 rounded-full"></div>
			</div>
		</div>

		<div class="absolute bottom-20 left-10 opacity-20 hidden lg:block">
			<div class="w-24 h-48 bg-gray-400 rounded-lg transform rotate-12"></div>
		</div>

		<!-- Stethoscope Visual Element -->
		<div
			class="absolute top-1/2 right-20 transform -translate-y-1/2 opacity-40 hidden xl:block"
		>
			<div class="relative">
				<!-- Stethoscope tubing -->
				<div class="w-2 h-64 bg-blue-500 rounded-full transform rotate-12"></div>
				<div
					class="absolute -top-8 -left-6 w-16 h-16 border-4 border-blue-500 rounded-full bg-white"
				></div>
				<div
					class="absolute -bottom-8 -right-6 w-12 h-12 border-4 border-blue-500 rounded-full bg-white"
				></div>
			</div>
		</div>

		<!-- Header -->
		<header class="relative z-10 bg-white/90 backdrop-blur-sm border-b border-gray-200">
			<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
				<div class="flex justify-between items-center py-4">
					<!-- Logo -->
					<div class="flex items-center">
						<div class="text-xl sm:text-2xl font-bold">
							<span class="text-cyan-500">connect</span>
							<span class="text-blue-600">2</span>
							<span class="text-cyan-500">clinic</span>
						</div>
					</div>

					<!-- Contact Info & Navigation -->
					<div class="hidden md:flex items-center space-x-4 lg:space-x-6">
						<div class="flex items-center text-gray-600 text-sm">
							<svg
								class="w-4 h-4 text-pink-500 mr-2"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
								></path>
							</svg>
							<span>1800 267 9899</span>
						</div>
						<div class="flex items-center text-gray-600 text-sm">
							<svg
								class="w-4 h-4 text-pink-500 mr-2"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
								></path>
							</svg>
							<span>hello@connect2clinic.com</span>
						</div>
						<div class="flex items-center text-gray-600 text-sm cursor-pointer">
							<svg
								class="w-4 h-4 text-pink-500 mr-2"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
								></path>
							</svg>
							<span>Home Page</span>
							<svg
								class="w-4 h-4 ml-1"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M19 9l-7 7-7-7"
								></path>
							</svg>
						</div>
					</div>

					<!-- Mobile Menu Button -->
					<button class="md:hidden p-2">
						<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 6h16M4 12h16M4 18h16"
							></path>
						</svg>
					</button>
				</div>
			</div>
		</header>

		<!-- Main Content -->
		<main class="relative z-10 flex items-center justify-center pt-20 pb-20">
			<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
				<!-- Role Selection Buttons -->
				<div class="flex justify-center mb-8 sm:mb-12">
					<div class="bg-white rounded-full p-1 shadow-lg">
						<button
							@click="selectedRole = 'doctor'"
							:class="[
								'px-6 py-3 rounded-full text-sm font-medium transition-all duration-200',
								selectedRole === 'doctor'
									? 'bg-gray-100 text-gray-800 shadow-sm'
									: 'text-gray-600 hover:text-gray-800',
							]"
						>
							I'm a Doctor
						</button>
						<button
							@click="selectedRole = 'patient'"
							:class="[
								'px-6 py-3 rounded-full text-sm font-medium transition-all duration-200',
								selectedRole === 'patient'
									? 'bg-cyan-500 text-white shadow-lg'
									: 'text-gray-600 hover:text-gray-800',
							]"
						>
							I'm a Patient
						</button>
					</div>
				</div>

				<!-- Main Heading -->
				<h1
					class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-8 sm:mb-16"
				>
					Hello, How can we help you?
				</h1>

				<!-- Search Section -->
				<div class="max-w-2xl mx-auto">
					<div class="relative mb-6">
						<input
							v-model="searchQuery"
							type="text"
							placeholder="Search Your Query"
							class="w-full px-6 py-4 pr-14 text-lg rounded-full border border-gray-300 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent shadow-lg"
						/>
						<button
							@click="handleSearch"
							class="absolute right-2 top-1/2 transform -translate-y-1/2 bg-cyan-500 text-white p-3 rounded-full hover:bg-cyan-600 transition-colors duration-200"
						>
							<svg
								class="w-5 h-5"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
								></path>
							</svg>
						</button>
					</div>

					<!-- Popular Searches -->
					<div class="text-white text-sm sm:text-base">
						<span class="opacity-80">Popular Searches: </span>
						<button
							class="hover:text-cyan-300 transition-colors duration-200 underline"
						>
							Account Setup
						</button>
						<span class="mx-2">•</span>
						<button
							class="hover:text-cyan-300 transition-colors duration-200 underline"
						>
							Appointment Cancellation
						</button>
					</div>
				</div>
			</div>
		</main>

		<!-- Laptop Visual Element -->
		<div class="absolute bottom-10 left-10 opacity-30 hidden lg:block">
			<div class="w-32 h-20 bg-gray-700 rounded-t-lg"></div>
			<div class="w-36 h-2 bg-gray-600 rounded-b-xl -mt-1"></div>
		</div>

		<!-- FAQ Section -->
		<div class="min-h-screen bg-gray-50">
			<!-- Navigation Tabs -->
			<div class="bg-white border-b">
				<div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
					<div class="flex space-x-8 overflow-x-auto">
						<button
							@click="activeTab = 'questions'"
							:class="[
								'py-4 px-2 text-sm font-medium border-b-2 whitespace-nowrap transition-colors duration-200',
								activeTab === 'questions'
									? 'border-red-500 text-gray-900'
									: 'border-transparent text-gray-500 hover:text-gray-700',
							]"
						>
							Most Asked Questions
						</button>
						<button
							@click="activeTab = 'categories'"
							:class="[
								'py-4 px-2 text-sm font-medium border-b-2 whitespace-nowrap transition-colors duration-200',
								activeTab === 'categories'
									? 'border-red-500 text-gray-900'
									: 'border-transparent text-gray-500 hover:text-gray-700',
							]"
						>
							Categories
						</button>
					</div>
				</div>
			</div>

			<!-- Main Content -->
			<div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
				<!-- Most Asked Questions Section -->
				<div v-if="activeTab === 'questions'" class="space-y-8">
					<div class="text-center mb-12">
						<h1 class="text-3xl font-bold text-gray-900 mb-2">Most Asked Questions</h1>
					</div>

					<!-- FAQ Accordion -->
					<div class="space-y-4">
						<div
							v-for="(faq, index) in faqs"
							:key="index"
							class="bg-white rounded-lg shadow-sm border"
						>
							<button
								@click="toggleFaq(index)"
								class="w-full px-6 py-5 text-left flex justify-between items-center hover:bg-gray-50 transition-colors duration-200"
							>
								<span class="text-gray-800 font-medium pr-4">{{
									faq.question
								}}</span>
								<svg
									:class="[
										'w-5 h-5 text-gray-500 transition-transform duration-200 flex-shrink-0',
										openFaq === index ? 'transform rotate-45' : '',
									]"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M12 6v6m0 0v6m0-6h6m-6 0H6"
									></path>
								</svg>
							</button>

							<div
								v-if="openFaq === index"
								class="px-6 pb-5 text-gray-600 leading-relaxed"
							>
								{{ faq.answer }}
							</div>
						</div>
					</div>
				</div>

				<!-- Categories Section -->
				<div v-if="activeTab === 'categories'" class="space-y-8">
					<div class="text-center mb-12">
						<h1 class="text-3xl font-bold text-gray-900 mb-8">Categories</h1>

						<!-- Category Filters -->
						<div class="flex flex-wrap justify-center gap-4 mb-8">
							<button
								v-for="category in categories"
								:key="category.id"
								@click="selectedCategory = category.id"
								:class="[
									'px-6 py-3 rounded-full text-sm font-medium transition-all duration-200 flex items-center space-x-2',
									selectedCategory === category.id
										? 'bg-red-500 text-white shadow-lg'
										: 'bg-white text-gray-600 border border-gray-300 hover:border-gray-400 hover:text-gray-800',
								]"
							>
								<component :is="getCategoryIcon(category.icon)" class="w-4 h-4" />
								<span>{{ category.name }}</span>
							</button>
						</div>
					</div>

					<!-- Related Questions Section -->
					<div class="bg-white rounded-lg shadow-sm border p-6">
						<h2 class="text-xl font-semibold text-gray-900 mb-6">Related Questions</h2>

						<div class="space-y-4">
							<div
								v-for="(question, index) in filteredQuestions"
								:key="index"
								class="border-b border-gray-200 last:border-b-0"
							>
								<button
									@click="toggleRelatedQuestion(index)"
									class="w-full py-4 text-left flex justify-between items-center hover:text-gray-600 transition-colors duration-200"
								>
									<span class="text-gray-700 font-medium pr-4">{{
										question.question
									}}</span>
									<svg
										:class="[
											'w-5 h-5 text-gray-400 transition-transform duration-200 flex-shrink-0',
											openRelatedQuestion === index
												? 'transform rotate-45'
												: '',
										]"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M12 6v6m0 0v6m0-6h6m-6 0H6"
										></path>
									</svg>
								</button>

								<div
									v-if="openRelatedQuestion === index"
									class="pb-4 text-gray-600 leading-relaxed"
								>
									{{ question.answer }}
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const selectedRole = ref('patient')
const searchQuery = ref('')
const activeTab = ref('questions')
const openFaq = ref(null)
const openRelatedQuestion = ref(null)
const selectedCategory = ref('ALL')

// FAQ data
const faqs = ref([
	{
		question: 'Is the e-prescription compliant to the tele consultation guidelines?',
		answer: 'Yes, our e-prescription system is fully compliant with telemedicine guidelines set by medical regulatory authorities. All prescriptions include necessary patient information, doctor credentials, and follow proper formatting standards.',
	},
	{
		question: 'Can I download the prescription after consultation?',
		answer: 'Absolutely! After your consultation is complete, you can download your prescription in PDF format directly from your patient dashboard. The prescription will be digitally signed and can be used at any pharmacy.',
	},
	{
		question: 'Can I book appointment with anyone within India?',
		answer: 'Yes, you can book appointments with any registered healthcare provider across India through our platform. Our network includes doctors from various specialties in all major cities and towns.',
	},
	{
		question: 'Does Connect2clinic decide the fees for online consultation?',
		answer: 'No, individual healthcare providers set their own consultation fees. Connect2clinic provides the platform but doctors maintain full control over their pricing. You can see the consultation fee before booking.',
	},
	{
		question:
			'I am not able to view my upcoming appointments with the doctor or past appointments taken.',
		answer: "Please try refreshing your browser or logging out and back in. If the issue persists, check your internet connection or contact our support team. Your appointment history should be visible in the 'My Appointments' section of your dashboard.",
	},
])

// Categories data
const categories = ref([
	{ id: 'ALL', name: 'ALL', icon: 'AllIcon' },
	{ id: 'CONSULTATION', name: 'CONSULTATION', icon: 'ConsultationIcon' },
	{ id: 'COMPLIANCE', name: 'COMPLIANCE', icon: 'ComplianceIcon' },
	{ id: 'GETTING_STARTED', name: 'GETTING STARTED', icon: 'GetStartedIcon' },
	{ id: 'APPOINTMENT', name: 'APPOINTMENT', icon: 'AppointmentIcon' },
])

// Related questions data with updated content
const relatedQuestions = ref([
	{
		question: 'Will online doctors be able to solve my medical issue?',
		answer: 'Our doctors will give you qualified medical advice on your health issues and help you identify the next steps, which may include further tests, a prescription, or lifestyle tips. You can use features like medical records/image sharing, voice calling and video call to ensure that doctors get all the required information for a diagnosis. In some cases on doctor discretion you will be asked for in-person visit, clinical & diagnostic tests.',
		category: 'CONSULTATION',
	},
	{
		question:
			'Is online medical consultation with doctor private on the platform? Is my data secure?',
		answer: 'Yes, all consultations are completely private and secure. We use end-to-end encryption and comply with healthcare data protection standards. Your medical information is never shared with third parties without your consent.',
		category: 'COMPLIANCE',
	},
	{
		question: 'Are online consultations legal?',
		answer: 'Yes, online consultations are legal and regulated by medical authorities. Our platform follows all telemedicine guidelines and regulations set by healthcare regulatory bodies.',
		category: 'COMPLIANCE',
	},
	{
		question: 'Are your doctors qualified?',
		answer: 'All doctors on our platform are verified medical professionals with valid licenses. We conduct thorough background checks and verify credentials before onboarding any healthcare provider.',
		category: 'COMPLIANCE',
	},
	{
		question: 'Are there any guidelines that I have to adhere to online?',
		answer: 'Yes, please ensure you have a stable internet connection, are in a quiet private space, have your medical history ready, and follow the consultation etiquette guidelines provided.',
		category: 'GETTING_STARTED',
	},
	{
		question: 'How does an online consultation work?',
		answer: 'Book an appointment, join the video call at scheduled time, discuss your health concerns with the doctor, receive digital prescription if needed, and follow up as recommended.',
		category: 'GETTING_STARTED',
	},
	{
		question: 'How to get started?',
		answer: 'Create an account, complete your profile, search for a doctor by specialty, book an appointment, and join the video call at the scheduled time.',
		category: 'GETTING_STARTED',
	},
	{
		question: 'I have booked my appointment, how do I log in at the time of my consultation?',
		answer: 'You will receive an email and SMS with the consultation link. Simply click the link at your appointment time or log into your account and join from your dashboard.',
		category: 'APPOINTMENT',
	},
	{
		question: 'Can I book appointment with doctor anytime I want to?',
		answer: 'You can book appointments based on doctor availability. Most doctors have flexible schedules including evenings and weekends. Some offer same-day appointments.',
		category: 'APPOINTMENT',
	},
])

// Computed property for filtered questions
const filteredQuestions = computed(() => {
	if (selectedCategory.value === 'ALL') {
		return relatedQuestions.value
	}
	return relatedQuestions.value.filter((q) => q.category === selectedCategory.value)
})

// Methods
const handleSearch = () => {
	if (searchQuery.value.trim()) {
		console.log('Searching for:', searchQuery.value)
		// Add your search logic here
	}
}

const toggleFaq = (index) => {
	openFaq.value = openFaq.value === index ? null : index
}

const toggleRelatedQuestion = (index) => {
	openRelatedQuestion.value = openRelatedQuestion.value === index ? null : index
}

// Function to get category icons
const getCategoryIcon = (iconName) => {
	const icons = {
		AllIcon: {
			template: `<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"></path></svg>`,
		},
		ConsultationIcon: {
			template: `<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>`,
		},
		ComplianceIcon: {
			template: `<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>`,
		},
		GetStartedIcon: {
			template: `<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>`,
		},
		AppointmentIcon: {
			template: `<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>`,
		},
	}
	return icons[iconName] || icons.AllIcon
}
</script>

<style scoped>
/* Additional custom styles if needed */
.bg-gradient-to-br {
	background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
}

/* Custom scrollbar for category tabs */
.overflow-x-auto::-webkit-scrollbar {
	height: 4px;
}

.overflow-x-auto::-webkit-scrollbar-track {
	background: #f1f1f1;
}

.overflow-x-auto::-webkit-scrollbar-thumb {
	background: #c1c1c1;
	border-radius: 2px;
}

.overflow-x-auto::-webkit-scrollbar-thumb:hover {
	background: #a1a1a1;
}
</style>
