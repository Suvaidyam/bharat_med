<template>
	<div class="min-h-screen bg-gray-50 p-4 lg:p-6">
		<div class="">
			<!-- Header -->
			<div class="bg-white rounded-sm shadow-sm mb-6 p-6">
				<div class="flex flex-col lg:flex-row lg:items-center lg:justify-between mb-6">
					<div>
						<h1 class="text-2xl font-bold text-gray-900 mb-2">Patient Reviews</h1>
						<p class="text-gray-600">
							Manage and moderate patient feedback about the clinic
						</p>
					</div>
					<div class="flex flex-col sm:flex-row gap-3 mt-4 lg:mt-0">
						<button
							class="px-4 py-2 border border-gray-300 rounded-sm text-gray-700 hover:bg-gray-50 flex items-center gap-2"
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
									d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
								></path>
							</svg>
							Export
						</button>
						<button
							class="px-4 py-2 bg-gray-900 text-white rounded-sm hover:bg-gray-800"
						>
							Respond to Feedback
						</button>
					</div>
				</div>

				<!-- Tabs -->
				<div class="flex flex-wrap gap-6 border-b border-gray-200">
					<button
						v-for="tab in tabs"
						:key="tab.id"
						@click="activeTab = tab.id"
						:class="[
							'pb-3 px-1 text-sm font-medium border-b-2 transition-colors',
							activeTab === tab.id
								? 'border-blue-500 text-blue-600'
								: 'border-transparent text-gray-500 hover:text-gray-700',
						]"
					>
						{{ tab.name }}
					</button>
				</div>
			</div>

			<!-- Search Bar -->
			<div class="bg-white rounded-sm shadow-sm mb-6 p-4">
				<div class="relative">
					<svg
						class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400"
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
					<input
						v-model="searchQuery"
						type="text"
						placeholder="Search reviews..."
						class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
					/>
				</div>
			</div>

			<div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
				<!-- Review Statistics -->
				<div class="lg:col-span-1">
					<div class="bg-white rounded-sm shadow-sm p-6 sticky top-6">
						<h2 class="text-lg font-semibold text-gray-900 mb-2">Review Statistics</h2>
						<p class="text-sm text-gray-600 mb-6">
							Overview of patient reviews and ratings
						</p>

						<!-- Overall Rating -->
						<div class="text-center mb-6">
							<div class="text-4xl font-bold text-gray-900 mb-2">
								{{ overallRating }}
							</div>
							<div class="flex justify-center mb-2">
								<div class="flex">
									<svg
										v-for="i in 5"
										:key="i"
										:class="[
											'w-5 h-5',
											i <= Math.floor(overallRating)
												? 'text-yellow-400'
												: 'text-gray-300',
										]"
										fill="currentColor"
										viewBox="0 0 20 20"
									>
										<path
											d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
										></path>
									</svg>
								</div>
							</div>
							<p class="text-sm text-gray-600">
								Based on {{ totalReviews }} reviews
							</p>
						</div>

						<!-- Rating Breakdown -->
						<div class="space-y-3">
							<div
								v-for="rating in ratingBreakdown"
								:key="rating.stars"
								class="flex items-center gap-3"
							>
								<span class="text-sm text-gray-600 w-6">{{ rating.stars }}</span>
								<span class="text-sm text-gray-500">stars</span>
								<div class="flex-1 bg-gray-200 rounded-full h-2">
									<div
										:style="{ width: rating.percentage + '%' }"
										class="bg-gray-800 h-2 rounded-full"
									></div>
								</div>
								<span class="text-sm text-gray-600 w-8"
									>{{ rating.percentage }}%</span
								>
							</div>
						</div>
					</div>
				</div>

				<!-- Reviews List -->
				<div class="lg:col-span-3">
					<!-- Filters -->
					<div class="bg-white rounded-sm shadow-sm p-4 mb-6">
						<div class="flex flex-col gap-4">
							<!-- Dropdowns -->
							<div
								class="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between"
							>
								<div class="flex flex-col sm:flex-row gap-4">
									<div class="flex items-center gap-2">
										<span class="text-sm text-gray-600">Filter by:</span>
										<select
											v-model="selectedRating"
											class="border border-gray-300 rounded-sm px-3 py-1 text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
										>
											<option value="">All Ratings</option>
											<option value="5">5 Stars</option>
											<option value="4">4 Stars</option>
											<option value="3">3 Stars</option>
											<option value="2">2 Stars</option>
											<option value="1">1 Star</option>
										</select>
									</div>
									<select
										v-model="selectedCategory"
										class="border border-gray-300 rounded-sm px-3 py-1 text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
									>
										<option value="">All Categories</option>
										<option value="general">General</option>
										<option value="wait-times">Wait Times</option>
										<option value="facilities">Facilities</option>
										<option value="staff">Staff</option>
									</select>
									<select
										v-model="selectedService"
										class="border border-gray-300 rounded-sm px-3 py-1 text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
									>
										<option value="">All Services</option>
										<option value="outpatient">Outpatient</option>
										<option value="consultation">Consultation</option>
										<option value="emergency">Emergency</option>
										<option value="surgery">Surgery</option>
									</select>
								</div>
								<span class="text-sm text-gray-600"
									>Showing {{ filteredReviews.length }} of
									{{ reviews.length }} reviews</span
								>
							</div>

							<!-- Status Toggles -->
							<div
								class="flex flex-col sm:flex-row gap-4 items-start sm:items-center"
							>
								<span class="text-sm text-gray-600">Show status:</span>
								<div class="flex flex-wrap gap-4">
									<label class="flex items-center gap-2 cursor-pointer">
										<div class="relative">
											<input
												v-model="showApproved"
												type="checkbox"
												class="sr-only"
											/>
											<div
												:class="[
													'w-8 h-4 rounded-full transition-colors',
													showApproved ? 'bg-green-500' : 'bg-gray-300',
												]"
											>
												<div
													:class="[
														'w-3 h-3 bg-white rounded-full transition-transform duration-200 ease-in-out mt-0.5',
														showApproved
															? 'translate-x-4 ml-0.5'
															: 'translate-x-0.5',
													]"
												></div>
											</div>
										</div>
										<span class="text-sm text-gray-700">Approved</span>
									</label>

									<label class="flex items-center gap-2 cursor-pointer">
										<div class="relative">
											<input
												v-model="showPending"
												type="checkbox"
												class="sr-only"
											/>
											<div
												:class="[
													'w-8 h-4 rounded-full transition-colors',
													showPending ? 'bg-yellow-500' : 'bg-gray-300',
												]"
											>
												<div
													:class="[
														'w-3 h-3 bg-white rounded-full transition-transform duration-200 ease-in-out mt-0.5',
														showPending
															? 'translate-x-4 ml-0.5'
															: 'translate-x-0.5',
													]"
												></div>
											</div>
										</div>
										<span class="text-sm text-gray-700">Pending</span>
									</label>

									<label class="flex items-center gap-2 cursor-pointer">
										<div class="relative">
											<input
												v-model="showFlagged"
												type="checkbox"
												class="sr-only"
											/>
											<div
												:class="[
													'w-8 h-4 rounded-full transition-colors',
													showFlagged ? 'bg-red-500' : 'bg-gray-300',
												]"
											>
												<div
													:class="[
														'w-3 h-3 bg-white rounded-full transition-transform duration-200 ease-in-out mt-0.5',
														showFlagged
															? 'translate-x-4 ml-0.5'
															: 'translate-x-0.5',
													]"
												></div>
											</div>
										</div>
										<span class="text-sm text-gray-700">Flagged</span>
									</label>
								</div>
							</div>
						</div>
					</div>

					<!-- Review Cards -->
					<div class="space-y-4">
						<div
							v-for="review in filteredReviews"
							:key="review.id"
							class="bg-white rounded-sm shadow-sm p-6 hover:shadow-md transition-shadow"
						>
							<div class="flex items-start justify-between mb-4">
								<div class="flex items-start gap-4">
									<div
										class="w-10 h-10 bg-gray-300 rounded-full flex items-center justify-center"
									>
										<svg
											class="w-6 h-6 text-gray-600"
											fill="none"
											stroke="currentColor"
											viewBox="0 0 24 24"
										>
											<path
												stroke-linecap="round"
												stroke-linejoin="round"
												stroke-width="2"
												d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
											></path>
										</svg>
									</div>
									<div>
										<h3 class="font-semibold text-gray-900 mb-1">
											{{ review.title }}
										</h3>
										<div class="flex items-center gap-2 mb-2">
											<div class="flex">
												<svg
													v-for="i in 5"
													:key="i"
													:class="[
														'w-4 h-4',
														i <= review.rating
															? 'text-yellow-400'
															: 'text-gray-300',
													]"
													fill="currentColor"
													viewBox="0 0 20 20"
												>
													<path
														d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
													></path>
												</svg>
											</div>
											<span class="text-sm text-gray-600">{{
												review.date
											}}</span>
											<span
												:class="[
													'px-2 py-1 text-xs rounded-full',
													review.status === 'approved'
														? 'bg-green-100 text-green-800'
														: review.status === 'pending'
															? 'bg-yellow-100 text-yellow-800'
															: 'bg-red-100 text-red-800',
												]"
											>
												{{
													review.status.charAt(0).toUpperCase() +
													review.status.slice(1)
												}}
											</span>
										</div>
									</div>
								</div>
								<button class="text-gray-400 hover:text-gray-600">
									<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
										<path
											d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
										></path>
									</svg>
								</button>
							</div>

							<div class="mb-4">
								<p class="text-sm text-gray-600 mb-2">
									Review by {{ review.reviewer }}
								</p>
								<p class="text-gray-800">{{ review.content }}</p>
							</div>

							<!-- Actions -->
							<div
								class="flex items-center justify-between pt-4 border-t border-gray-200"
							>
								<div class="flex items-center gap-4">
									<button
										class="flex items-center gap-1 text-sm text-gray-600 hover:text-gray-800"
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
												d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5"
											></path>
										</svg>
										Helpful ({{ review.helpful }})
									</button>
									<button
										class="flex items-center gap-1 text-sm text-blue-600 hover:text-blue-800"
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
												d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6"
											></path>
										</svg>
										Respond
									</button>
								</div>
								<div class="flex items-center gap-4 text-sm text-gray-500">
									<span>Category: {{ review.category }}</span>
									<span>Service: {{ review.service }}</span>
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
const activeTab = ref('all')
const searchQuery = ref('')
const selectedRating = ref('')
const selectedCategory = ref('')
const selectedService = ref('')
const showApproved = ref(true)
const showPending = ref(true)
const showFlagged = ref(true)

// Static data
const tabs = [
	{ id: 'all', name: 'All Reviews' },
	{ id: 'pending', name: 'Pending Moderation' },
	{ id: 'flagged', name: 'Flagged' },
]

const overallRating = ref(3.3)
const totalReviews = ref(6)

const ratingBreakdown = [
	{ stars: 5, percentage: 33 },
	{ stars: 4, percentage: 17 },
	{ stars: 3, percentage: 17 },
	{ stars: 2, percentage: 17 },
	{ stars: 1, percentage: 17 },
]

const reviews = ref([
	{
		id: 1,
		title: 'Excellent care and facilities',
		rating: 5,
		date: '15/04/2023',
		status: 'approved',
		reviewer: 'Michael Thompson',
		content:
			'I had an amazing experience at the clinic. The staff was friendly and professional, and the facilities were clean and modern. The wait time was minimal, and I received excellent care.',
		helpful: 18,
		category: 'General',
		service: 'Outpatient',
	},
	{
		id: 2,
		title: 'Good doctors but long wait times',
		rating: 3,
		date: '10/04/2023',
		status: 'approved',
		reviewer: 'Emily Wilson',
		content:
			'The doctors and nurses were very professional and knowledgeable. However, I had to wait over an hour past my scheduled appointment time, which was frustrating. Better scheduling would improve the experience.',
		helpful: 7,
		category: 'Wait Times',
		service: 'Consultation',
	},
	{
		id: 3,
		title: 'Poor service quality',
		rating: 2,
		date: '08/04/2023',
		status: 'pending',
		reviewer: 'John Davis',
		content:
			'The reception staff was rude and unhelpful. Had to wait 2 hours for a simple consultation. The facility needs better management and customer service training.',
		helpful: 3,
		category: 'Staff',
		service: 'Consultation',
	},
	{
		id: 4,
		title: 'Clean facilities, professional staff',
		rating: 4,
		date: '05/04/2023',
		status: 'approved',
		reviewer: 'Sarah Brown',
		content:
			'Overall good experience. The clinic is very clean and well-maintained. Staff members were professional and courteous. Only minor issue was parking availability.',
		helpful: 12,
		category: 'Facilities',
		service: 'Outpatient',
	},
])

// Computed properties
const filteredReviews = computed(() => {
	return reviews.value.filter((review) => {
		const matchesSearch =
			review.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			review.content.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			review.reviewer.toLowerCase().includes(searchQuery.value.toLowerCase())

		const matchesRating =
			!selectedRating.value || review.rating === parseInt(selectedRating.value)

		const matchesCategory =
			!selectedCategory.value ||
			review.category.toLowerCase() === selectedCategory.value.toLowerCase()

		const matchesService =
			!selectedService.value ||
			review.service.toLowerCase() === selectedService.value.toLowerCase()

		const matchesStatus =
			(showApproved.value && review.status === 'approved') ||
			(showPending.value && review.status === 'pending') ||
			(showFlagged.value && review.status === 'flagged')

		return matchesSearch && matchesRating && matchesCategory && matchesService && matchesStatus
	})
})
</script>
