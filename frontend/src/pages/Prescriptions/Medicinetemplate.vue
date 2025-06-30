<template>
	<div class="min-h-screen">
		<!-- Header -->
		<div class="bg-white px-6 py-4">
			<div class="flex items-center justify-between">
				<div class="flex items-center">
					<button class="mr-3 text-gray-400 hover:text-gray-600">
						<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M15 19l-7-7 7-7"
							></path>
						</svg>
					</button>
					<div>
						<h1 class="text-xl font-semibold text-gray-900">Medicine Templates</h1>
						<p class="text-sm text-gray-600 mt-1">
							Manage reusable medication templates for prescriptions.
						</p>
					</div>
				</div>
				<button
					class="bg-black text-white px-4 py-2 rounded-sm hover:bg-gray-800 transition-colors"
				>
					New Template
				</button>
			</div>
		</div>

		<div class="p-6">
			<!-- Tabs -->
			<div class="mb-6">
				<nav class="flex space-x-8">
					<button
						v-for="tab in tabs"
						:key="tab.id"
						@click="activeTab = tab.id"
						:class="[
							'py-2 px-1 border-b-2 font-medium text-sm transition-colors',
							activeTab === tab.id
								? 'border-black text-gray-900'
								: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
						]"
					>
						{{ tab.name }}
					</button>
				</nav>
			</div>

			<!-- All Templates Section -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200 mb-6">
				<!-- Section Header -->
				<div class="px-6 py-4 border-b border-gray-200">
					<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
						<div>
							<h2 class="text-lg font-semibold text-gray-900">All Templates</h2>
							<p class="text-sm text-gray-600 mt-1">
								Browse and manage all medication templates.
							</p>
						</div>
						<div class="flex items-center gap-3 mt-4 sm:mt-0">
							<!-- Search -->
							<div class="relative">
								<div
									class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
								>
									<svg
										class="h-4 w-4 text-gray-400"
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
								</div>
								<input
									v-model="searchQuery"
									type="text"
									placeholder="Search templates..."
									class="pl-10 pr-4 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm w-64"
								/>
							</div>
						</div>
					</div>
				</div>

				<!-- Templates Table -->
				<div class="overflow-x-auto">
					<table class="w-full">
						<thead class="bg-gray-50 border-b border-gray-200">
							<tr>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Template Name
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Category
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Medications
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Created By
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Last Used
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Usage
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Actions
								</th>
							</tr>
						</thead>
						<tbody class="bg-white divide-y divide-gray-200">
							<tr
								v-for="template in filteredTemplates"
								:key="template.id"
								@click="selectedTemplate = template"
								:class="[
									'hover:bg-gray-50 cursor-pointer transition-colors',
									selectedTemplate?.id === template.id ? 'bg-blue-50' : '',
								]"
							>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm font-medium text-gray-900">
										{{ template.name }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										:class="getCategoryClass(template.category)"
										class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
									>
										{{ template.category }}
									</span>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900 text-center">
										{{ template.medicationCount }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ template.createdBy }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ template.lastUsed }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900 text-center">
										{{ template.usage }} times
									</div>
								</td>
								<td
									class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
								>
									<button
										class="text-gray-400 hover:text-gray-600 transition-colors"
									>
										<svg
											class="h-5 w-5"
											fill="none"
											stroke="currentColor"
											viewBox="0 0 24 24"
										>
											<path
												stroke-linecap="round"
												stroke-linejoin="round"
												stroke-width="2"
												d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"
											></path>
										</svg>
									</button>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>

			<!-- Template Details Section -->
			<div
				v-if="selectedTemplate"
				class="bg-white rounded-lg shadow-sm border border-gray-200 mb-6"
			>
				<div class="px-6 py-4 border-b border-gray-200">
					<div class="flex items-center justify-between">
						<div>
							<h2 class="text-lg font-semibold text-gray-900">Template Details</h2>
							<p class="text-sm text-gray-600 mt-1">
								View detailed information about a selected template.
							</p>
						</div>
						<div class="flex items-center gap-2">
							<button
								class="p-2 text-gray-400 hover:text-gray-600 transition-colors"
							>
								<svg
									class="h-4 w-4"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
									></path>
								</svg>
							</button>
							<button
								class="bg-black text-white px-4 py-2 rounded-sm hover:bg-gray-800 transition-colors text-sm"
							>
								Use Template
							</button>
						</div>
					</div>
				</div>

				<div class="p-6">
					<!-- Template Header -->
					<div class="mb-6">
						<h3 class="text-xl font-semibold text-gray-900 mb-2">
							{{ selectedTemplate.name }}
						</h3>
						<div class="flex items-center gap-4 text-sm text-gray-600">
							<span
								>{{ selectedTemplate.category }} • Created by
								{{ selectedTemplate.createdBy }}</span
							>
						</div>
					</div>

					<!-- Medications Section -->
					<div class="mb-6">
						<h4 class="text-lg font-medium text-gray-900 mb-4">Medications</h4>
						<div class="space-y-4">
							<div
								v-for="medication in selectedTemplateDetails.medications"
								:key="medication.id"
								class="border border-gray-200 rounded-lg p-4"
							>
								<h5 class="font-medium text-gray-900 mb-3">
									{{ medication.name }}
								</h5>
								<div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
									<div>
										<span class="text-gray-500">Route:</span>
										<div class="font-medium text-gray-900">
											{{ medication.route }}
										</div>
									</div>
									<div>
										<span class="text-gray-500">Frequency:</span>
										<div class="font-medium text-gray-900">
											{{ medication.frequency }}
										</div>
									</div>
									<div>
										<span class="text-gray-500">Duration:</span>
										<div class="font-medium text-gray-900">
											{{ medication.duration }}
										</div>
									</div>
								</div>
								<div v-if="medication.instructions" class="mt-3">
									<span class="text-gray-500 text-sm">Instructions:</span>
									<div class="text-sm text-gray-900 mt-1">
										{{ medication.instructions }}
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- Usage Statistics -->
					<div>
						<h4 class="text-lg font-medium text-gray-900 mb-4">Usage Statistics</h4>
						<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
							<div class="text-center">
								<div class="text-2xl font-bold text-gray-900">
									{{ selectedTemplate.usage }}
								</div>
								<div class="text-sm text-gray-500">Total Uses</div>
							</div>
							<div class="text-center">
								<div class="text-2xl font-bold text-gray-900">
									{{ selectedTemplate.lastUsed }}
								</div>
								<div class="text-sm text-gray-500">Last Used</div>
							</div>
							<div class="text-center">
								<div class="text-2xl font-bold text-gray-900">
									{{ selectedTemplate.createdDate }}
								</div>
								<div class="text-sm text-gray-500">Created On</div>
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
const searchQuery = ref('')
const activeTab = ref('all')
const selectedTemplate = ref(null)

// Tabs configuration
const tabs = ref([
	{ id: 'all', name: 'All Templates' },
	{ id: 'recent', name: 'Recently Used' },
	{ id: 'my', name: 'My Templates' },
])

// Sample templates data
const templates = ref([
	{
		id: 1,
		name: 'Hypertension Standard',
		category: 'Cardiovascular',
		medicationCount: 2,
		createdBy: 'Dr. Sarah Johnson',
		lastUsed: '2024-03-15',
		usage: 42,
		createdDate: '2023-05-10',
	},
	{
		id: 2,
		name: 'Diabetes Type 2',
		category: 'Endocrine',
		medicationCount: 1,
		createdBy: 'Dr. Michael Chen',
		lastUsed: '2024-04-02',
		usage: 38,
		createdDate: '2023-06-15',
	},
	{
		id: 3,
		name: 'Antibiotic - Respiratory',
		category: 'Infectious Disease',
		medicationCount: 1,
		createdBy: 'Dr. Lisa Patel',
		lastUsed: '2024-03-28',
		usage: 27,
		createdDate: '2023-07-20',
	},
	{
		id: 4,
		name: 'Pain Management - Mild',
		category: 'Pain Management',
		medicationCount: 2,
		createdBy: 'Dr. James Wilson',
		lastUsed: '2024-04-10',
		usage: 31,
		createdDate: '2023-08-05',
	},
	{
		id: 5,
		name: 'Asthma Management',
		category: 'Respiratory',
		medicationCount: 2,
		createdBy: 'Dr. Emily Rodriguez',
		lastUsed: '2024-03-30',
		usage: 24,
		createdDate: '2023-09-12',
	},
	{
		id: 6,
		name: 'Allergy - Seasonal',
		category: 'Allergy',
		medicationCount: 1,
		createdBy: 'Dr. Sarah Johnson',
		lastUsed: '2024-04-05',
		usage: 19,
		createdDate: '2023-10-18',
	},
])

// Template details (for the selected template)
const selectedTemplateDetails = computed(() => {
	if (!selectedTemplate.value) return null

	// Mock detailed data based on selected template
	const details = {
		1: {
			// Hypertension Standard
			medications: [
				{
					id: 1,
					name: 'Lisinopril 10mg',
					route: 'Oral',
					frequency: 'Once daily',
					duration: '30 days',
					instructions: 'Take in the morning with or without food',
				},
				{
					id: 2,
					name: 'Hydrochlorothiazide 12.5mg',
					route: 'Oral',
					frequency: 'Once daily',
					duration: '30 days',
					instructions: 'Take in the morning with food',
				},
			],
		},
		2: {
			// Diabetes Type 2
			medications: [
				{
					id: 1,
					name: 'Metformin 500mg',
					route: 'Oral',
					frequency: 'Twice daily',
					duration: '30 days',
					instructions: 'Take with meals to reduce stomach upset',
				},
			],
		},
	}

	return details[selectedTemplate.value.id] || { medications: [] }
})

// Computed properties
const filteredTemplates = computed(() => {
	return templates.value.filter((template) => {
		const searchTerm = searchQuery.value.toLowerCase()
		return (
			template.name.toLowerCase().includes(searchTerm) ||
			template.category.toLowerCase().includes(searchTerm) ||
			template.createdBy.toLowerCase().includes(searchTerm)
		)
	})
})

// Helper functions
const getCategoryClass = (category) => {
	const categoryColors = {
		Cardiovascular: 'bg-red-100 text-red-800',
		Endocrine: 'bg-purple-100 text-purple-800',
		'Infectious Disease': 'bg-yellow-100 text-yellow-800',
		'Pain Management': 'bg-orange-100 text-orange-800',
		Respiratory: 'bg-blue-100 text-blue-800',
		Allergy: 'bg-green-100 text-green-800',
	}
	return categoryColors[category] || 'bg-gray-100 text-gray-800'
}

// Initialize with first template selected
selectedTemplate.value = templates.value[0]
</script>
