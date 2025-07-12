<template>
	<div class="bg-gray-50 min-h-screen font-sans text-gray-800">
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
			<!-- Page Header -->
			<header class="mb-8">
				<h1 class="text-3xl font-bold text-gray-900">Support Center</h1>
				<p class="mt-1 text-gray-600">
					Get help with your clinic management system or submit a support ticket.
				</p>
			</header>

			<!-- Tabs -->
			<div class="mb-6">
				<div class="bg-gray-200/75 rounded-lg p-1 inline-flex items-center gap-1">
					<button
						@click="activeTab = 'new'"
						:class="[
							'px-6 py-2 rounded-md text-sm font-semibold transition-colors duration-200',
							activeTab === 'new'
								? 'bg-white text-gray-900 shadow-sm'
								: 'text-gray-600 hover:bg-white/50',
						]"
					>
						New Ticket
					</button>
					<button
						@click="activeTab = 'my'"
						:class="[
							'px-6 py-2 rounded-md text-sm font-semibold transition-colors duration-200',
							activeTab === 'my'
								? 'bg-white text-gray-900 shadow-sm'
								: 'text-gray-600 hover:bg-white/50',
						]"
					>
						My Tickets
					</button>
					<button
						@click="activeTab = 'faq'"
						:class="[
							'px-6 py-2 rounded-md text-sm font-semibold transition-colors duration-200',
							activeTab === 'faq'
								? 'bg-white text-gray-900 shadow-sm'
								: 'text-gray-600 hover:bg-white/50',
						]"
					>
						FAQ
					</button>
				</div>
			</div>

			<!-- Form Card -->
			<div class="bg-white border border-gray-200 rounded-lg p-6 md:p-8">
				<div class="mb-6">
					<h2 class="text-xl font-bold text-gray-900">Submit a Support Ticket</h2>
					<p class="mt-1 text-sm text-gray-600">
						Fill out the form below to create a new support ticket. Our team will
						respond as soon as possible.
					</p>
				</div>

				<form @submit.prevent="submitTicket">
					<div class="space-y-6">
						<!-- Row 1: Subject & Category -->
						<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
							<div>
								<label
									for="subject"
									class="block text-sm font-medium text-gray-700"
									>Subject</label
								>
								<input
									type="text"
									id="subject"
									v-model="form.subject"
									class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
									placeholder="Brief description of the issue"
								/>
							</div>
							<div>
								<label
									for="category"
									class="block text-sm font-medium text-gray-700"
									>Category</label
								>
								<select
									id="category"
									v-model="form.category"
									class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
								>
									<option value="" disabled>Select category</option>
									<option>Billing Issue</option>
									<option>Technical Problem</option>
									<option>Feature Request</option>
									<option>General Question</option>
								</select>
							</div>
						</div>

						<!-- Row 2: Priority -->
						<div>
							<label for="priority" class="block text-sm font-medium text-gray-700"
								>Priority</label
							>
							<select
								id="priority"
								v-model="form.priority"
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
							>
								<option value="" disabled>Select priority</option>
								<option>Low</option>
								<option>Medium</option>
								<option>High</option>
								<option>Urgent</option>
							</select>
						</div>

						<!-- Row 3: Description -->
						<div>
							<label
								for="description"
								class="block text-sm font-medium text-gray-700"
								>Description</label
							>
							<textarea
								id="description"
								rows="4"
								v-model="form.description"
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
								placeholder="Please provide detailed information about your issue"
							></textarea>
						</div>

						<!-- Row 4: Attachments -->
						<div>
							<label
								for="attachments"
								class="block text-sm font-medium text-gray-700"
								>Attachments (optional)</label
							>
							<div class="mt-1">
								<input
									type="file"
									id="attachments"
									class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-gray-100 file:text-gray-700 hover:file:bg-gray-200"
								/>
							</div>
							<p class="mt-1 text-xs text-gray-500">
								You can upload screenshots or documents to help explain your issue
								(max 5MB per file)
							</p>
						</div>
					</div>

					<!-- Form Actions -->
					<div
						class="mt-8 pt-5 border-t border-gray-200 flex justify-end items-center gap-x-3"
					>
						<button
							type="button"
							class="px-4 py-2 text-sm font-semibold text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
						>
							Cancel
						</button>
						<button
							type="submit"
							class="px-4 py-2 text-sm font-semibold text-white bg-gray-800 rounded-md shadow-sm hover:bg-gray-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-900"
						>
							Submit Ticket
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const activeTab = ref('new')

const form = reactive({
	subject: '',
	category: '',
	priority: '',
	description: '',
	attachments: null,
})

const submitTicket = () => {
	// A real application would send this data to a server
	console.log('Submitting ticket:', { ...form })
	alert('Ticket submitted! (Check the console for data)')
}
</script>

<style scoped>
/* Scoping styles to prevent conflicts */
/* Add any component-specific, non-Tailwind styles here if needed */
</style>
