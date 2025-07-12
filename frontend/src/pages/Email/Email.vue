<template>
	<div class="min-h-screen bg-gray-50 flex">
		<!-- Sidebar -->
		<div class="w-64 bg-white shadow-sm border-r border-gray-200 flex flex-col">
			<!-- Header -->
			<div class="px-4 py-6 border-b border-gray-200">
				<h1 class="text-xl font-semibold text-gray-900">Email</h1>
			</div>

			<!-- Navigation -->
			<nav class="flex-1 px-4 py-6 space-y-1">
				<button
					v-for="item in sidebarItems"
					:key="item.id"
					@click="setActiveSection(item.id)"
					:class="[
						'w-full flex items-center px-3 py-2 text-sm font-medium rounded-md transition-colors',
						activeSection === item.id
							? 'bg-gray-100 text-gray-900'
							: 'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
					]"
				>
					<span class="mr-3">{{ item.icon }}</span>
					{{ item.label }}
				</button>
			</nav>

			<!-- Labels -->
			<div class="px-4 py-6 border-t border-gray-200">
				<h3 class="text-sm font-medium text-gray-900 mb-3">Labels</h3>
				<div class="space-y-2">
					<div
						v-for="label in labels"
						:key="label.id"
						class="flex items-center text-sm text-gray-600"
					>
						<div :class="['w-3 h-3 rounded-full mr-3', label.color]"></div>
						{{ label.label }}
					</div>
				</div>
			</div>
		</div>

		<!-- Main Content -->
		<div class="flex-1 flex flex-col">
			<!-- Top Bar -->
			<div
				class="bg-white border-b border-gray-200 px-6 py-4 flex items-center justify-between"
			>
				<div class="flex items-center space-x-4">
					<div class="relative">
						<input
							v-model="searchQuery"
							type="text"
							placeholder="Search emails..."
							class="w-80 pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
						/>
						<svg
							class="absolute left-3 top-2.5 h-5 w-5 text-gray-400"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
							/>
						</svg>
					</div>
				</div>
				<button
					class="bg-black text-white px-4 py-2 rounded-md hover:bg-gray-800 transition-colors flex items-center"
				>
					<svg
						class="w-4 h-4 mr-2"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M12 4v16m8-8H4"
						/>
					</svg>
					Compose
				</button>
			</div>

			<!-- Email List -->
			<div class="flex-1 overflow-auto">
				<div class="divide-y divide-gray-200">
					<div v-if="currentEmails.length === 0" class="p-8 text-center text-gray-500">
						<svg
							class="mx-auto h-12 w-12 text-gray-400 mb-4"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2m-14 0H2"
							/>
						</svg>
						<h3 class="text-lg font-medium text-gray-900 mb-1">
							No emails in {{ getSectionTitle.toLowerCase() }}
						</h3>
						<p class="text-sm text-gray-500">
							When you receive emails, they'll appear here.
						</p>
					</div>

					<div
						v-for="email in currentEmails"
						:key="email.id"
						class="p-4 hover:bg-gray-50 cursor-pointer border-l-4 border-transparent hover:border-blue-500 transition-all"
					>
						<div class="flex items-start justify-between">
							<div class="flex items-start space-x-3 flex-1">
								<input
									type="checkbox"
									class="mt-1 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
								/>
								<div class="flex-1 min-w-0">
									<div class="flex items-center justify-between mb-1">
										<p class="text-sm font-medium text-gray-900 truncate">
											{{ email.from || `To: ${email.to}` }}
										</p>
										<div class="flex items-center space-x-2">
											<span v-if="email.isImportant" class="text-yellow-400"
												>⚠️</span
											>
											<span v-if="email.isStarred" class="text-yellow-400"
												>⭐</span
											>
											<span class="text-xs text-gray-500">{{
												email.time
											}}</span>
										</div>
									</div>
									<p class="text-sm font-medium text-gray-900 mb-1">
										{{ email.subject }}
									</p>
									<p class="text-sm text-gray-500 line-clamp-1">
										{{ email.preview }}
									</p>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- Pagination -->
				<div
					class="px-6 py-3 bg-white border-t border-gray-200 flex items-center justify-between"
				>
					<span class="text-sm text-gray-700">Page 1 of 1</span>
					<div class="flex items-center space-x-2">
						<button
							class="p-2 text-gray-400 hover:text-gray-600 disabled:opacity-50"
							disabled
						>
							<svg
								class="w-4 h-4"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 19l-7-7 7-7"
								/>
							</svg>
						</button>
						<button
							class="p-2 text-gray-400 hover:text-gray-600 disabled:opacity-50"
							disabled
						>
							<svg
								class="w-4 h-4"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M9 5l7 7-7 7"
								/>
							</svg>
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

const activeSection = ref('inbox')
const searchQuery = ref('')

const sidebarItems = [
	{ id: 'inbox', icon: '📥', label: 'Inbox' },
	{ id: 'sent', icon: '📤', label: 'Sent' },
	{ id: 'draft', icon: '📝', label: 'Draft' },
	{ id: 'bin', icon: '🗑️', label: 'Bin' },
	{ id: 'archive', icon: '📦', label: 'Archive' },
	{ id: 'important', icon: '⚠️', label: 'Important' },
	{ id: 'starred', icon: '⭐', label: 'Starred' },
]

const labels = [
	{ id: 'patient', color: 'bg-red-500', label: 'Patient' },
	{ id: 'admin', color: 'bg-blue-500', label: 'Admin' },
	{ id: 'lab', color: 'bg-green-500', label: 'Lab' },
	{ id: 'pharmacy', color: 'bg-yellow-500', label: 'Pharmacy' },
	{ id: 'insurance', color: 'bg-purple-500', label: 'Insurance' },
]

const inboxEmails = [
	{
		id: 1,
		from: 'dr.johnson@medixpro.com',
		subject: 'Your Recent Test Results',
		preview:
			"Dear Mr. Smith, I'm pleased to inform you that your recent blood tests came back normal. No further action is needed at this time.",
		time: 'about 2 years ago',
		isImportant: false,
		isStarred: false,
	},
	{
		id: 2,
		from: 'admin@medixpro.com',
		subject: 'Staff Meeting - April 20th',
		preview:
			'Dear Dr. Johnson, This is a reminder about the upcoming staff meeting on April 20th at 9:00 AM in Conference Room A.',
		time: 'about 2 years ago',
		isImportant: true,
		isStarred: true,
	},
	{
		id: 3,
		from: 'insurance@healthcare.com',
		subject: 'Claim #87654 - Additional Information Required',
		preview:
			'We need additional documentation for claim #87654. Please provide the requested information within 14 days.',
		time: 'about 2 years ago',
		isImportant: true,
		isStarred: false,
	},
	{
		id: 4,
		from: 'dr.smith@medixpro.com',
		subject: 'Patient Referral - Cardiology Consultation',
		preview:
			"I'm referring Patient #54321 to you for a cardiology consultation. Patient records attached.",
		time: 'about 2 years ago',
		isImportant: false,
		isStarred: true,
	},
	{
		id: 5,
		from: 'hr@medixpro.com',
		subject: 'Annual Leave Balance Update',
		preview:
			'This is a reminder that you have 15 days of annual leave remaining that must be used before December 31st.',
		time: 'over 2 years ago',
		isImportant: false,
		isStarred: false,
	},
]

const sentEmails = [
	{
		id: 1,
		to: 'pharmacy@medixpro.com',
		subject: 'Prescription Refill for Patient #12345',
		preview:
			"Please prepare a refill for Patient #12345's hypertension medication. The prescription details are attached.",
		time: 'about 2 years ago',
	},
	{
		id: 2,
		to: 'lab@medixpro.com',
		subject: 'Lab Test Request for Patient #67890',
		preview:
			'Please schedule a comprehensive metabolic panel for Patient #67890 at their earliest convenience.',
		time: 'about 2 years ago',
	},
	{
		id: 3,
		to: 'it@medixpro.com',
		subject: 'Technical Issue with Patient Portal',
		preview:
			"I'm experiencing difficulties accessing the patient portal. Could you please assist?",
		time: 'about 2 years ago',
	},
]

const currentEmails = computed(() => {
	switch (activeSection.value) {
		case 'sent':
			return sentEmails
		case 'draft':
			return []
		case 'bin':
			return []
		case 'archive':
			return []
		case 'important':
			return inboxEmails.filter((email) => email.isImportant)
		case 'starred':
			return inboxEmails.filter((email) => email.isStarred)
		default:
			return inboxEmails
	}
})

const setActiveSection = (section) => {
	activeSection.value = section
}

const getSectionTitle = computed(() => {
	const section = sidebarItems.find((item) => item.id === activeSection.value)
	return section ? section.label : 'Inbox'
})
</script>
